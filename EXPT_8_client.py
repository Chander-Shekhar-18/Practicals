import rpyc
import sys

def main():
    c = rpyc.connect("localhost", 18862)
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    print('Sum of', x ,'&', y, 'is:', c.root.add(x, y))
    print('Difference of', x ,'&', y, 'is:', c.root.sub(x, y))
    print('Product of', x ,'&', y, 'is:', c.root.mul(x, y))
    print('Quotient of', x ,'&', y, 'is:', c.root.div(x, y))

if __name__ == "__main__":
    main()
