# Nim
# Isaac Cheung
class Minimax:
    def __init__(self, nimState, minMaxLevel):
        
        # initializes the class Minimax
        
        self.state = nimState
        self.level = minMaxLevel
        self.child = []
        self.build_tree()
        
    def build_tree(self):
        
        # builds the tree of possible states
        
        if self.level == 'MAX':
            next_level = 'MIN'
        elif self.level == 'MIN':
            next_level = 'MAX'
        
        possibilities = self.split(self.state)
        for event in possibilities:
            
            # for every new possible state create another tree of possible states
            
            new_state = Minimax(event,next_level)
            self.add_child(new_state)
                
    def add_child(self, item):
        self.child.append(item)
        
    def split(self, pile):
        
        # creates a list of all possible states and returns the list
        
        total_pile = []
        pile_index = 0
        pile.sort()     # by sorting beforehand it makes it easy to clean up
        while pile_index < len(pile):
            single_pile = pile[pile_index]
            remainder = pile[:pile_index] + pile[pile_index+1:]
            splitted_pile = self.single_split(single_pile)
            pile_index += 1
            for item in splitted_pile:
                for remains in remainder:
                    item.append(remains)
                item.sort()
                total_pile.append(item)
        while pile in total_pile:
            total_pile.remove(pile) # prevents duplicates of the pile in the new pile
        return total_pile    
    
    def single_split(self, single_pile):
        
        # 6 returns [[1,3],[2,4]]
        # takes an int and returns possible states in list of lists form
        split_pile = []
        if single_pile < 3:
            split_pile.append([single_pile])
        else:
            first = 1
            last = single_pile - 1
            if single_pile % 2 == 0:
                mid = single_pile//2
            else:
                mid = (single_pile//2)+1  
            while first < mid :
                split_pile.append([first,last])
                first += 1
                last -= 1
        return split_pile
        
    def print_tree(self,indent, last):
        
        # prints the tree
        
        print(indent, end = '')
        
        if last:
            print('\-', end = '')
            indent += '  '
        else:
            print('+ ', end = '')
            indent += '| '
        status = str(self.state)
        if last:
            status = status + ' ' + self.level
        
        print(status)
        for child in self.child:
            last = False
            if child == self.child[-1] :
                last = True
            
            child.print_tree(indent, last)
def main():
    user = 0
    level = 'MAX'
    while user <= 2:
        try:
            user = int(input('Choose your initial size of the pile. Should be more than 2: '))
        except:
            pass
        
    # construct the tree    
    new_pile = Minimax([user],level)
    
    # build the tree
    indent = '   '
    last = True
    new_pile.print_tree(indent,last)
    
    input("press anything to close")
main()
