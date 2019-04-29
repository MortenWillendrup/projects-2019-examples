from scipy import optimize

def solve_for_ss(s,g,n,alpha,delta):
    """ delete all non-municipalities

    Args:
        df (pd.DataFrame): pandas dataframe with the column "municipality" as a string

    Returns:
        df (pd.DataFrame): pandas dataframe

    """ 
    
    # a. define objective function
    f = lambda k: k**alpha
    obj_kss = lambda kss: kss - (s*f(kss) + (1-delta)*kss)/((1+g)*(1+n))

    #. b. call root finder
    result = optimize.root_scalar(obj_kss,bracket=[0.1,100],method='bisect')
    return result