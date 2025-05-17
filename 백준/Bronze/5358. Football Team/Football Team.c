#include <stdio.h>
#include <string.h>

int main(void) {

	char line[100];
	
	while (fgets(line, sizeof(line), stdin) != NULL) {
		
		size_t len = strlen(line);
		
		if (line[len - 1] == '\n') {
			line[len - 1] = '\0';
		}

		for (size_t i=0; line[i]!= '\0'; i++) {
			if (line[i]=='i') {
				line[i] = 'e';
			}else if(line[i]=='I') {
				line[i] = 'E';
			}else if (line[i]=='e') {
				line[i] = 'i';
			}else if(line[i]=='E') {
				line[i] = 'I';
			}
		}
		
		printf("%s\n", line);
	}
	return 0;
}