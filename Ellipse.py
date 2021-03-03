import sys
import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rnd
from matplotlib.patches import Ellipse
sys.path.append(".")
from Random import Gaussian


# main function for our coin toss Python code
if __name__ == "__main__":

    # default number of samples (per experiment)
    Nsample = 1

    if '-h' in sys.argv or '--help' in sys.argv or not haveH0:
        print ("Usage: %s [options]" % sys.argv[0])
        print ("  options:")
        print ("   --help(-h)          print options")
        print ("   -Nsample [number] number of samples for each experiment")
        print
        sys.exit(1)

    if '-Nsample' in sys.argv:
        p = sys.argv.index('-Nsample')
        Ns = int(sys.argv[p+1])
        if Ns > 0:
            Nsample = Ns


    G1 = Gaussian(seed =1, mu=0, sigma=5)
    G2 = Gaussian(seed =2, mu=0, sigma=3)
    Sample1 = G1.Gaussian_sample(0,Nsample)
    Sample2 = G2.Gaussian_sample(0,Nsample)
    E_sample = []
    E_reject = []
    for i in range(Sample1.shape[0]):
        x = Sample1[i]
        y = Sample2[i]
        if (x**2/25+y**2/9)<4 :
            E_sample.append((x,y))
        else :
            E_reject.append((x,y))
    E_sample =np.array(E_sample)
    E_reject =np.array(E_reject)
    E=Ellipse(xy=(0,0), width=20, height=12)

    fig = plt.figure(0)
    fig.suptitle(str(E_sample.shape[0]/Nsample)+'% acceptance rate')
    ax = fig.add_subplot(111, aspect='equal')
    ax.add_artist(E)
    E.set_alpha(0.3)
    E.set_facecolor('b')

    ax.scatter(E_sample[:,0], E_sample[:,1], c='r',marker = '.' , s=10)
    ax.scatter(E_reject[:,0], E_reject[:,1], c='g',marker = '.', s=10)

    ax.set_xlim(-15, 15)
    ax.set_ylim(-10, 10)

    plt.savefig('Ellipse_sample.png')
    plt.show()
    
    
    
    
    
    
    
