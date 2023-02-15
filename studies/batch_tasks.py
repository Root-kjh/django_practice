import requests
from rest_framework.exceptions import ValidationError

from .serializers import StudySerializer

def get_studies_num():
    """
    clinicaltrials.gov 에 존재하는 임상 연구 개수를 가져오는 메소드
    """
    CLINICALTRIALS_STATISTICS_URL = 'https://clinicaltrials.gov/api/info/study_statistics'
    response = requests.get(CLINICALTRIALS_STATISTICS_URL, params={'fmt': 'json'})
    studies_num = int(response.json()['StudyStatistics']['ElmtDefs']['Study']['nInstances'])
    return studies_num

def get_studies(start, end):
    """
    clinicaltrials.gov 에서 제공하는 API 에서 임상 연구 목록을 가져오는 메소드
    """
    CLINICALTRIALS_OPEN_API_BASE_URL = 'https://clinicaltrials.gov/api/query/full_studies'
    response = requests.get(CLINICALTRIALS_OPEN_API_BASE_URL, params={'fmt': 'json', 'min_rnk': start, 'max_rnk': end})
    response_json = response.json()
    if response_json['FullStudiesResponse']['NStudiesFound'] == 0:
        return []
    return response_json['FullStudiesResponse']['FullStudies']

def convert_study(study):
    description_module = study['Study']['ProtocolSection'].get('DescriptionModule', {})

    if 'OfficialTitle' in description_module:
        title = description_module['OfficialTitle']
    elif 'BriefTitle' in description_module:
        title = description_module['BriefTitle']
    elif 'BriefSummary' in description_module:
        title = description_module['BriefSummary']
    else:
        title = None

    interventions = study['Study']['ProtocolSection'].get('InterventionModule', {}).get('InterventionList', {}).get('Intervention', [])
    conditions = study['Study']['ProtocolSection'].get('ConditionModule', {}).get('ConditionList', {}).get('Condition', [])
    eligibility_module = study['Study']['ProtocolSection'].get('EligibilityModule', None)
    if eligibility_module is None:
        eligibility = []
    else:
        eligibility = [
            {
                'gender': eligibility_module.get('Gender', None),
                'minimum_age': eligibility_module.get('MinimumAge', None),
                'maximum_age': eligibility_module.get('MaximumAge', None),
                'healthy_volunteers': eligibility_module.get('HealthyVolunteers', None),
                'criteria': eligibility_module.get('EligibilityCriteria', None),
            }
        ]
    return {
        'nct_id': study['Study']['ProtocolSection']['IdentificationModule']['NCTId'],
        'title': title,
        'results_first_submitted_date': description_module.get('ResultsFirstSubmittedDate', None),
        'last_update_submitted_date': description_module.get('LastUpdateSubmittedDate', None),
        'start_date': description_module.get('StartDate', None),
        'completion_date': description_module.get('CompletionDate', None),
        'overall_status': description_module.get('OverallStatus', None),
        'phase': description_module.get('Phase', None),
        'enrollment': description_module.get('Enrollment', None),
        'intervensions': [
            {
                'intervention_type': intervention.get('InterventionType', None),
                'name': intervention.get('InterventionName', None),
                'description': intervention.get('Description', None),
            }
            for intervention in interventions
        ],
        'conditions': [
            condition['Condition']
            for condition in conditions
        ],
        'eligibilities': eligibility,
    }

def save_all_studies():
    """
    clinicaltrials.gov 에서 제공하는 API 에서 전체 임상 연구 목록을 저장하는 메소드
    """
    studies_num = get_studies_num()
    for start in range(1, studies_num, 100):
        end = start + 99
        studies = get_studies(start, end)
        for study in studies:
            study = convert_study(study)
            study_serializer = StudySerializer(data=study)
            try:
                study_serializer.is_valid(raise_exception=True)
            except ValidationError as e:
                if e.detail.get('nct_id', None) is not None and e.detail['nct_id'][0].code == 'unique':
                    continue
                raise e
            study_serializer.save()