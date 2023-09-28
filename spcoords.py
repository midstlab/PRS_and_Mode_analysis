def superposer(value_x, value_y):
    import numpy as np
    from Bio.SVDSuperimposer import SVDSuperimposer
    from numpy import array, dot, set_printoptions
    x = np.array(value_x , 'f')
    y = np.array(value_y, 'f')
    superpose = SVDSuperimposer()
    #set the coords initial will be rotated and translated on final coordinates
    superpose.set(x, y)
    superpose.run()
    rms = superpose.get_rms()
    
    #get rotation (right multiplying!) and the translation
    rot, tran = superpose.get_rotran()
    
    #Rotate initial to final
    initial_on_final = dot(y, rot) + tran
    
    #same thing
    initial_on_final_2 = superpose.get_transformed()
    """
    set_printoptions(precision=2)
    print(initial_on_final)
    print(initial_on_final_2)
    print("%.2f" % rms)
    """
    #return superpose.set
    return initial_on_final,rms
    