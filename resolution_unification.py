# 1D array to 2D and split.
def line_to_sentence(_line): 
    _list = []
    for i in range(len(_line)):
        for x in _line[i]:
            if x == ",":
                _line[i] = str(_line[i][0:_line[i].index(x)-1])
                break
        _list.append(_line[i].split(") "))
        
    return _list

# Create a dictionary of sentence_list that we got
def create_dict(sentence):
    _dict = {}
    tmp = []
    

    for i in range(len(sentence)):
        tmp = []
        for j in range(len(sentence[i])):
            tmp2 = []
            var_counter = 0
            if "!" in sentence[i][j]:
                tmp2.append(1)
            elif "!" not in sentence[i][j]:
                tmp2.append(-1)
            for each in sentence[i][j]:
                if ord(each) >= 96 and ord(each) <=122:
                    var_counter += 1
            tmp2.append(var_counter)
            if "!" in sentence[i][j] and sentence[i][j][-2] != ")":
                tmp2.append(sentence[i][j]+") ")
            elif sentence[i][j][-1] != ")":
                tmp2.append(sentence[i][j]+") ")
            else:
                tmp2.append(sentence[i][j])
            tmp.append(tmp2)
            _dict[i+1] = tmp
    return _dict

def BFS_iteration(_line):
    #BFS Search Approach
    sentence_list = line_to_sentence(_line)
    _dict = create_dict(sentence_list)

    tmp_line = []
    for i in range(1, len(_line)+1):
        for j in range(i+1, len(_line)+1):
            for x in range(len(_dict[i])):
                for c in range(len(_dict[j])):
                    predicate_i = ""
                    predicate_j = ""
                    var_i = ""
                    var_j =""
                    final_resol_i = ""
                    final_resol_j = ""
                    resol = ""
                    for value in _dict[i][x][2]:
                        if ord(value) >= 65 and ord(value) <=90:
                            predicate_i += value
            
                        elif ord(value) >= 96 and ord(value) <=122:
                            var_i += value
                    for value in _dict[j][c][2]:
                        
                        if ord(value) >= 65 and ord(value) <=90:
                            predicate_j += value
                    
                        elif ord(value) >= 96 and ord(value) <=122:
                            var_j += value
                    #if negation is different, num of var is same, and predicates are same => resolution
                    if predicate_i == predicate_j and _dict[i][x][0] != _dict[j][c][0] and _dict[i][x][1] == _dict[j][c][1]:
                        #compare the length of each values and remove the predicate of the greater key.

                        for k in range(len(_dict[i])):
                            if k != x:
                                final_resol_i += _dict[i][k][2]
                        for g in range(len(_dict[j])):
                            if g != c:
                                final_resol_j += _dict[j][g][2]
                        resol = final_resol_i + final_resol_j
                        
                        addition = ""

                        for varNum in range(len(var_i)):
                            #pass if same
                            if var_i[varNum] == var_j[varNum]:
                                pass

                            elif var_i[varNum] in variable_list and var_j[varNum] in variable_list:
                                addition += ", "+var_i[varNum]+"/"+var_j[varNum]
                                resol = resol.replace(var_i[varNum], var_j[varNum])
                                
                            elif var_i[varNum] in variable_list and var_j[varNum] not in variable_list:
                                addition += ", "+var_i[varNum]+"/"+var_j[varNum]
                                resol = resol.replace(var_i[varNum], var_j[varNum])

                            elif var_i[varNum] not in variable_list and var_j[varNum] in variable_list:
                                addition += ", "+var_j[varNum]+"/"+var_i[varNum]
                                resol = resol.replace(var_j[varNum], var_i[varNum])

                            elif var_i[varNum] not in variable_list and var_j[varNum] not in variable_list:
                                addition += ", "+var_i[varNum]+"/"+var_j[varNum]
                                resol = resol.replace(var_i[varNum], var_j[varNum])

                        resol_result = (resol+", "+str(i)+" & "+str(j)) + addition
                        #ignore the duplicates
                        if resol_result not in final_result_BFS:
                            tmp_line.append(resol_result)
                        #Contradiction Handling
                        if ")" not in resol_result or "(" not in resol_result:
                            for tmp in range(len(tmp_line)-1):
                                lineByLine.append(tmp_line[tmp])
                                final_result_BFS.append(tmp_line[tmp])
                            for n in range(len(final_result_BFS)):
                                print(str(n+1)+". "+final_result_BFS[n]) 
                            print('By "' + resol_result[2:] + '" Contradiction occurred!')
                            return 
    
    for tmp in tmp_line:
        lineByLine.append(tmp)
        final_result_BFS.append(tmp)

    #Recursion
    BFS_iteration(lineByLine)
    
######################################################################################

def DFS_iteration(_line):
    _list = line_to_sentence(_line)
    current_dict = create_dict(_list)

    current_line = []
    for each in _line:
        current_line.append(each)

    for i in range(1, len(current_line)+1):
        for j in range(i+1, len(current_line)+1):
            for x in range(len(current_dict[i])):
                for c in range(len(current_dict[j])):
                    predicate_i = ""
                    predicate_j = ""
                    var_i = ""
                    var_j =""
                    final_resol_i = ""
                    final_resol_j = ""
                    resol = ""
                    for value in current_dict[i][x][2]:
                        if ord(value) >= 65 and ord(value) <=90:
                            predicate_i += value
            
                        elif ord(value) >= 96 and ord(value) <=122:
                            var_i += value
                    for value in current_dict[j][c][2]:
                        
                        if ord(value) >= 65 and ord(value) <=90:
                            predicate_j += value
                    
                        elif ord(value) >= 96 and ord(value) <=122:
                            var_j += value
                    #if negation is different, num of var is same, and predicates are same => resolution
                    if predicate_i == predicate_j and current_dict[i][x][0] != current_dict[j][c][0] and current_dict[i][x][1] == current_dict[j][c][1]:
                        #compare the length of each values and remove the predicate of the greater key.

                        for k in range(len(current_dict[i])):
                            if k != x:
                                final_resol_i += current_dict[i][k][2]
                        for g in range(len(current_dict[j])):
                            if g != c:
                                final_resol_j += current_dict[j][g][2]
                        resol = final_resol_i + final_resol_j
                        
                        addition = ""

                        for varNum in range(len(var_i)):
                            #pass if same
                            if var_i[varNum] == var_j[varNum]:
                                pass

                            elif var_i[varNum] in variable_list and var_j[varNum] in variable_list:
                                addition += ", "+var_i[varNum]+"/"+var_j[varNum]
                                resol = resol.replace(var_i[varNum], var_j[varNum])
                                
                            elif var_i[varNum] in variable_list and var_j[varNum] not in variable_list:
                                addition += ", "+var_i[varNum]+"/"+var_j[varNum]
                                resol = resol.replace(var_i[varNum], var_j[varNum])

                            elif var_i[varNum] not in variable_list and var_j[varNum] in variable_list:
                                addition += ", "+var_j[varNum]+"/"+var_i[varNum]
                                resol = resol.replace(var_j[varNum], var_i[varNum])

                            elif var_i[varNum] not in variable_list and var_j[varNum] not in variable_list:
                                addition += ", "+var_i[varNum]+"/"+var_j[varNum]
                                resol = resol.replace(var_i[varNum], var_j[varNum])


                        resol_result = (resol+", "+str(i)+" & "+str(j)) + addition
                        #ignore the duplicates
                        if resol_result not in final_result_DFS:
                            final_result_DFS.append(resol_result)
                            #Contradiction Handling
                            if ")" not in resol_result or "(" not in resol_result:
                                print('By "' + resol_result[2:] + '" Contradiction occurred!')
                                return 
                            print( str(len(final_result_DFS)) + ". " + resol_result)

                        result = DFS_iteration_deep(final_result_DFS)
                        if result == 1:
                            return

def DFS_iteration_deep(_line):
    _list = line_to_sentence(_line)
    _dict = create_dict(_list)
    current_dict = create_dict(_list)

    current_line = []
    for each in _line:
        current_line.append(each)

    for i in range(len(current_line), len(current_line)+1):
        for j in range(1, len(current_line)):
            for x in range(len(current_dict[i])):
                for c in range(len(current_dict[j])):
                    predicate_i = ""
                    predicate_j = ""
                    var_i = ""
                    var_j =""
                    final_resol_i = ""
                    final_resol_j = ""
                    resol = ""
                    for value in current_dict[i][x][2]:
                        if ord(value) >= 65 and ord(value) <=90:
                            predicate_i += value
            
                        elif ord(value) >= 96 and ord(value) <=122:
                            var_i += value
                    for value in current_dict[j][c][2]:
                        
                        if ord(value) >= 65 and ord(value) <=90:
                            predicate_j += value
                    
                        elif ord(value) >= 96 and ord(value) <=122:
                            var_j += value
                    #if negation is different, num of var is same, and predicates are same => resolution
                    if predicate_i == predicate_j and current_dict[i][x][0] != current_dict[j][c][0] and current_dict[i][x][1] == current_dict[j][c][1]:
                        #compare the length of each values and remove the predicate of the greater key.

                        for k in range(len(current_dict[i])):
                            if k != x:
                                final_resol_i += current_dict[i][k][2]
                        for g in range(len(current_dict[j])):
                            if g != c:
                                final_resol_j += current_dict[j][g][2]
                        resol = final_resol_i + final_resol_j
                        
                        addition = ""

                        for varNum in range(len(var_i)):
                            #pass if same
                            if var_i[varNum] == var_j[varNum]:
                                pass

                            elif var_i[varNum] in variable_list and var_j[varNum] in variable_list:
                                addition += ", "+var_i[varNum]+"/"+var_j[varNum]
                                resol = resol.replace(var_i[varNum], var_j[varNum])
                                
                            elif var_i[varNum] in variable_list and var_j[varNum] not in variable_list:
                                addition += ", "+var_i[varNum]+"/"+var_j[varNum]
                                resol = resol.replace(var_i[varNum], var_j[varNum])

                            elif var_i[varNum] not in variable_list and var_j[varNum] in variable_list:
                                addition += ", "+var_j[varNum]+"/"+var_i[varNum]
                                resol = resol.replace(var_j[varNum], var_i[varNum])

                            elif var_i[varNum] not in variable_list and var_j[varNum] not in variable_list:
                                addition += ", "+var_i[varNum]+"/"+var_j[varNum]
                                resol = resol.replace(var_i[varNum], var_j[varNum])

                        resol_result = (resol+", "+str(j)+" & "+str(i)) + addition

                        #ignore the duplicates
                        if resol_result not in final_result_DFS:
                            final_result_DFS.append(resol_result)
                            #Contradiction Handling
                            if ")" not in resol_result or "(" not in resol_result:
                                print('By "' + resol_result[2:] + '" Contradiction occurred!')
                                return 1
                            print( str(len(final_result_DFS)) + ". " + resol_result)

                        result = DFS_iteration_deep(final_result_DFS)
                        if result == 1:
                            return 1

#####################################################################################
# Start of BFS strategy

data = open("santa.txt", "r")
# data = open("howling-hounds.txt", "r")
lineByLine = [each.strip() for each in data.readlines()]
variable_list = ['u','v','w','x','y','z']

# print the given facts
line_num = 1
print('<BFS>\n')
print('---------- GIVEN FACTS ----------')
for fact in lineByLine:
    print(str(line_num) + '. ' + fact)
    line_num += 1
print('---------------------------------\n')
print("Negate the last fact to prove the theorem.")

# negate the last fact
if '!' in lineByLine[-1]:
    lineByLine[-1] = fact[3:-1]
else:
    lineByLine[-1] = '(! ' + fact + ')'

print('\n---------- START PROVING ----------')

final_result_BFS = []

for each in lineByLine:
    final_result_BFS.append(each)

BFS_iteration(final_result_BFS)


# Start of DFS strategy


data = open("santa.txt", "r")
# data = open("howling-hounds.txt", "r")
lineByLine = [each.strip() for each in data.readlines()]
variable_list = ['u','v','w','x','y','z']

# print the given facts
line_num = 1
print('\n<DFS>\n')
print('---------- GIVEN FACTS ----------')
for fact in lineByLine:
    print(str(line_num) + '. ' + fact)
    line_num += 1
print('---------------------------------\n')
print("Negate the last fact to prove the theorem.")

# negate the last fact
if '!' in lineByLine[-1]:
    lineByLine[-1] = fact[3:-1]
else:
    lineByLine[-1] = '(! ' + fact + ')'

# print the altered facts
line_num = 1
#lineByLine contains the final result. It will be updated as new resolution has been found
print('\n---------- START PROVING ----------')
for fact in lineByLine:
    print(str(line_num) + '. ' + fact)
    line_num += 1

final_result_DFS = []

for each in lineByLine:
    final_result_DFS.append(each)

DFS_iteration(final_result_DFS)