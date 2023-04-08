try:
    days = int(input('Enter No of Days : '))
except IndexError:
    print("Please pass 'days' argument in command line")
except ValueError:
    print("'Days' argument must be of integer type")
else:
    class Solution:
        def __init__(self, days):
            
            self.days = days
            self.ways_to_attend = self._ways_to_attend_classes()
        
        def number_of_ways_to_attend_classes(self):
            return len(self.ways_to_attend) - len(list(filter(lambda way: "AAAA" in way , self.ways_to_attend)))

        def probability_to_miss_gradution_ceremony(self):
             l= list(filter(lambda way: "AAAA" in way or way.endswith('A'), self.ways_to_attend))
             return len(l) - len(list(filter(lambda way: "AAAA" in way , self.ways_to_attend)))

        def _ways_to_attend_classes(self):
            li = []
            pattern = ""
            self._util(self.days, pattern, li)
            return li
        
        def _util(self, days, pattern, li):
            if days == 0:
                li.append(pattern)
            else:
                # At any given day there are only two possibalities
                self._util(days - 1, pattern + 'A', li)  # absent in class
                self._util(days - 1, pattern + 'P', li)  # present in class
        

    solution = Solution(days)
    x1 = solution.number_of_ways_to_attend_classes()
    x2 = solution.probability_to_miss_gradution_ceremony()

    print(f"for {days} days : {x2}/{x1}")

