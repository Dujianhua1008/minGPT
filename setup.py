# from setuptools import setup
#
# setup(name='minGPT',
#       version='0.0.1',
#       author='Andrej Karpathy',
#       packages=['mingpt'],
#       description='A PyTorch re-implementation of GPT',
#       license='MIT',
#       install_requires=[
#             'torch',
#       ],
# )


def merge( intervals):
        intervals.sort(key=lambda x: x[0])
        x=intervals.pop(0)
        result=[]
        while intervals :
            temp=intervals[0]
            a=x[0];b=x[1];c=temp[0];d=temp[1];
            if c>b+1 or d<a-1:
                result.append(x)
                x=temp
            elif (c>=a and c<=b)and(d>=b):
                x=[a,d]
            elif (c<=a and d>=b ):
                x=[c,d]
            elif c>=a and d<=b:
                x=[a,b]
            elif c<=a and (d<=b and d>=a):
                x=[c,b]
            intervals.pop(0)
        result.append(x)
        return result
nums=[[1,4],[0,0]]
print(merge(nums))
