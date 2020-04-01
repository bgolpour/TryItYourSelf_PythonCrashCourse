def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_desings = unprinted_designs.pop()
        print("Printing models are: " + current_desings )
        completed_models.append(current_desings)
def show_completed_models(completed_models):
    print("\n The following models have been printed:")
    for completed_model in completed_models:
        print(completed_models)
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []