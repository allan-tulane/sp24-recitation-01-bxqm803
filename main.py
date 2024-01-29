"""
CMPS 2200  Recitation 1
"""

### the only imports needed are here
import tabulate
import time
###


def linear_search(mylist, key):
  """ done. """
  for i, v in enumerate(mylist):
    if v == key:
      return i
  return -1


def binary_search(mylist, key):
  """ done. """
  return _binary_search(mylist, key, 0, len(mylist) - 1)


def _binary_search(mylist, key, left, right):
  if key>mylist[right] or key<mylist[left]:
    return -1
  index=int((right+left)//2)
  if mylist[index]<key :
    return _binary_search(mylist, key, index+1, right)
  elif mylist[index]>key :
    return _binary_search(mylist, key, left, index-1)
  elif mylist[index]==key :
    return index
  else :
    return -1



def time_search(search_fn, mylist, key):

  start=time.time()
  search_fn(mylist, key)
  end=time.time()
  res=1000*(end-start)
  return res
  
  


def compare_search(sizes=[1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]):

  res=[]
  for i in sizes :
    list1=list(range(0, i))
    linear=time_search(linear_search, list1, -1)
    binary=time_search(binary_search, list1, -1)
    tuple=(i, linear, binary,)
    res.append(tuple)
  return res
  """
  
	Compare the running time of linear_search and binary_search
	for input sizes as given. The key for each search should be
	-1. The list to search for each size contains the numbers from 0 to n-1,
	sorted in ascending order. 

	You'll use the time_search function to time each call.

	Returns:
	  A list of tuples of the form
	  (n, linear_search_time, binary_search_time)
	  indicating the number of milliseconds it takes
	  for each method to run on each value of n
	"""
  ### TODO

  ###


def print_results(results):
  """ done """
  print(
      tabulate.tabulate(results,
                        headers=['n', 'linear', 'binary'],
                        floatfmt=".3f",
                        tablefmt="github"))

sizes=[1,10,100,1000]
print_results(compare_search(sizes))