def init(network):
    # initialize the parameter
    import pickle
    with open('block0_greedy_RGB.txt', 'rb') as handle:
        block5_ = pickle.loads(handle.read())
    conv3_weight = block5_['conv3_weight']
    conv3_bias   = block5_['conv3_bias']
    conv2_weight = block5_['conv2_weight']
    conv2_bias   = block5_['conv2_bias']
    lin1_weight  = block5_['lin1_weight']
    lin1_bias    = block5_['lin1_bias']
    lin3_weight  = block5_['lin3_weight']
    lin3_bias    = block5_['lin3_bias']
    a_k          = block5_['a_k']
    b_k          = block5_['b_k']
    Haar          = block5_['Haar']


    k = 0
    i = 0 #block
    no_param = 11
    for f in network.parameters():
        if k == no_param*i:
            f.data = conv3_weight
            print('conv3_weight is',conv3_weight)
        elif k == no_param*i+1:
            #print('This is',k)
            f.data = conv3_bias
        elif k == no_param*i+2:
            #print('This is',k)
            f.data = conv2_weight
        elif k == no_param*i+3:
            #print('This is',k)
            f.data = conv2_bias
        elif k == no_param*i+4:
            #print('This is',k)
            f.data = lin1_weight
        elif k == no_param*i+5:
            #print('This is',k)
            f.data = lin1_bias
        elif k == no_param*i+6:
            #print('This is',k)
            f.data = lin3_weight
        elif k == no_param*i+7:
            #print('This is',k)
            f.data = lin3_bias
        elif k == no_param*i+8:
            #print('This is',k)
            f.data = a_k
        elif k == no_param*i+9:
            #print('This is',k)
            f.data = b_k
        elif k == no_param*i+10:
            #print('This is',k)
            f.data = Haar 
        k += 1  

