import seaborn as sns

def sort_two_lists(list1, list2):
    """Sort two lists based on values in list2.
    
    Args:
        list1: First list to sort
        list2: Second list to sort based on
        
    Returns:
        tuple: Sorted (list1, list2)
    """
    if len(list1) == 0:
        return [], []
        
    zipped_lists = zip(list1, list2)
    sorted_pairs = sorted(zipped_lists, key=lambda pair: pair[1])
    
    tuples = zip(*sorted_pairs)
    list1, list2 = [list(tuple) for tuple in tuples]
    return list1, list2

def get_children_concept_distribution(snomed_concepts, root_name, visualization=False):
    """Get distribution of concepts under a SNOMED-CT root concept.
    
    Args:
        snomed_concepts: Collection of SNOMED concepts
        root_name (str): Name of root concept to analyze
        visualization (bool): Whether to visualize distribution
        
    Returns:
        dict: Mapping of concept names to counts
    """
    level_1 = SNOMEDCT_US[root_name].children
    count_dic = {}
    
    for s_c in list(snomed_concepts):
        while s_c.parents:
            s_c = s_c.parents[0]
            if s_c in level_1:
                count_dic[s_c.name] = count_dic.get(s_c.name, 0) + 1
                break
                
    s_names, counts = sort_two_lists(list(count_dic.keys()), 
                                    list(count_dic.values()))
    s_labels = [str(SNOMEDCT_US[s_name].label[0]) for s_name in s_names]
    
    if s_names and visualization:
        sns.barplot(y=s_labels, x=counts)
        
    return {name: c for name, c in zip(s_labels, counts)} 