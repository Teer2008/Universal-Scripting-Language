import os

file_path = "src/test.usl"
file_content = []
calls = []
out_list = []
system_list = []
syscall_obj = []
print_ob = []
system_call_end = 0
print_ob_count = 0


with open(file_path, "r") as file:
    for line in file:
        word = line.split()

        file_content.extend(word)
        print(file_content)

file.close()

class reader:

    def shell_mode(self):
        if file_content[2] == '{':
            for item in file_content[3:]:
                calls.append(item)
            
            if calls[len(calls) == '}']:
                string_calls = ' '.join([str(elem) for elem in calls])
                string_calls = string_calls.replace('}', '')
                string_calls = string_calls.strip()
                os.system(string_calls)

    def lang_mode(self):
        if file_content[2] == '{':
            for item in file_content[3:]:
                calls.append(item)
            
            # Check Keywords
            for count, val in enumerate(calls):
                #Out KEYWORD
                if val == 'out:':
                    out_list.append(count)            
                    print_ob = [x+1 for x in out_list]
                    for x in range(len(print_ob)):
                        print(calls[print_ob[x]])
                
                #System KEYWORD
                if val == '#':
                    system_call_end = count
                    print(system_call_end)

                if val =='system:':
                    system_list.append(count)
                    print(system_list)
                    for i in calls[system_list[0]:system_call_end]:
                        syscall_obj.append(i)
                        print(syscall_obj)


    def low_level(self):
        if file_content[0] == 'mode:':
            if file_content[1] == 'shell':
                if file_content[2] == '{':
                    Keywords.shell_mode()
            
            if file_content[1] == 'baseLang':
                if file_content[2] == '{':
                    Keywords.lang_mode()

if __name__ == "__main__":
    Keywords = reader()
    Keywords.low_level()