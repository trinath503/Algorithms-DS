# get the input string

class Anagrams:

    def __init__(self):
        self.pragram_name = 'Find the Anagrams words '
        self.question_link = 'https://www.youtube.com/watch?v=psDooQ8Dwdo&t=17s'
        self.author = 'Trinath Reddy'
        self.map_word_indexs = {}
        self.given_strings_array = []
        self.anagrams = []

    '''
            @func        : for mapping matched string into dict
            @params      : NONE
            @operations  : calling print_results function 
            @return      : NONE
    '''
    def map_the_strings(self):
        for cur_indx, ele in enumerate(self.given_strings_array):
            # sort the string
            sorted_string = ''.join(sorted(ele))
            if sorted_string in self.map_word_indexs.keys():
                self.map_word_indexs[sorted_string].append(cur_indx)
            else:
                self.map_word_indexs[sorted_string] = [cur_indx]
        self.print_results()


    '''
        @func        : for getting inputs
        @params      : NONE
        @operations  : calling map_the_strings function 
        @return      : NONE
    '''
    def insert_strings(self):
        self.given_strings_array = list(map(str, input("Please enter words seperated by space:\n").split()))
        self.map_the_strings()

    '''
        @func        : for displaying results
        @params      : NONE
        @operations  : NONE
        @return      : NONE
    '''
    def print_results(self):
        for item in self.map_word_indexs.keys():
            # only matched results
            if len(self.map_word_indexs[item])==2:
                current_matched_lsit = []
                for each_map in self.map_word_indexs[item]:
                    current_matched_lsit.append(self.given_strings_array[each_map])
                self.anagrams.append(current_matched_lsit)
            else:
                print('No anagrams for word: ', item)
        # Finally print the results
        print(self.anagrams)

# creating the object
anagrams_object = Anagrams()
'''
    # calling the function
    # input  = cat dog god tac
    # output = [['cat', 'tac'], ['dog', 'god']] 
'''
anagrams_object.insert_strings()