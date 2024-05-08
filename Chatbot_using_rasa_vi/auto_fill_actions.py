import yaml,random

def generate_default_responses():
    list_text = [{'- text': 'Alright, I will take care of that.'},{'- text': "I'm currently processing your request."},{'- text':"I'm looking for the answer, I will reply to you as soon as possible"}]
    text = random.choice(list_text)
    return text

def auto_fill_actions(stories_file, domain_file):
    # Load stories.yml
    with open(stories_file, 'r', encoding='utf-8') as f:
        stories_data = yaml.safe_load(f)

    # Load domain.yml
    with open(domain_file, 'r', encoding='utf-8') as f:
        domain_data = yaml.safe_load(f)

    # Extract actions from stories.yml
    actions = set()
    for story in stories_data.get('stories', []):
        for step in story.get('steps', []):
            if 'action' in step:
                actions.add(step['action'])

    # Update responses in domain.yml
    for action in actions:
        if action not in domain_data['responses']:
            domain_data['responses'][action] = generate_default_responses()

    # Write updated domain.yml
    with open(domain_file, 'w') as f:
        yaml.dump(domain_data, f, default_flow_style=False)

def intents_miss(nlu_file,domain_file):
    # Load nlu.yml
    with open(nlu_file, 'r', encoding='utf-8') as f:
        nlu_data = yaml.safe_load(f)

    # Load new domain data
    with open(domain_file, 'r', encoding='utf-8') as f:
        domain_data = yaml.safe_load(f)

    
    nlu_intents = nlu_data.get('nlu', [])
    existing_intents = domain_data.get('intents', [])

    intents_miss = []
    for intent in nlu_intents:
        if intent not in existing_intents:
            intents_miss.append(intent.get('intent'))
    
    return intents_miss

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
merge_domain('domain_collector/domain_vie.yml', 'domain.yml')
