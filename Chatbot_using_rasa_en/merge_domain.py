import yaml,random
def merge_domain(n_domain_file, t_domain_file):
    # Load domain.yml
    with open(t_domain_file, 'r', encoding='utf-8') as f:
        domain_data = yaml.safe_load(f)

    # Load new domain data
    with open(n_domain_file, 'r', encoding='utf-8') as f:
        new_domain_data = yaml.safe_load(f)

    # Merge intents
    new_intents = new_domain_data.get('intents', [])
    existing_intents = domain_data.get('intents', [])
    for intent in new_intents:
        if intent not in existing_intents:
            existing_intents.append(intent)


    # Merge actions
    # new_actions = new_domain_data.get('actions', [])
    # existing_actions = domain_data.get('actions', [])
    # for action in new_actions:
    #     if action not in existing_actions:
    #         existing_actions.append(action)

    # Merge responses
    new_responses = new_domain_data.get('responses', {})
    existing_responses = domain_data.get('responses', {})
    for key, value in new_responses.items():
        if key not in existing_responses:
            existing_responses[key] = value

    # Update domain data
    domain_data['intents'] = existing_intents
    # domain_data['actions'] = existing_actions
    domain_data['responses'] = existing_responses

    # Write back to domain.yml
    with open(t_domain_file, 'w', encoding='utf-8') as f:
        yaml.dump(domain_data, f, default_flow_style=False, allow_unicode=True)

    print("Domain data merged successfully.")
# Usage example
merge_domain('UK/domain_collector/domain.yml', 'domain.yml')
