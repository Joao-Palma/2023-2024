#include <string.h>

#include <stdlib.h>

#include <stdio.h>

#define DEFANDLIB_H

#define MAXEST 20 

#define LICENSESIZE 8

#define MAXLINE 8192 //bytes

#define MINHOUR 60

#define MINDAY 60*24

#define MINYEAR 365*60*24

/*
---------------program structures---------------
*/

typedef struct {
    short day;
    short mon;  
    short year;
    short hour;
    short min;
    } Date;


typedef struct car{
    char *license;
    char *park;

    Date* entrydate;    
    Date* leavingdate;

    struct car *nextcar;
    } Car;

typedef struct park{
    char *name;
    int capac;
    int freespace;

    float value15;
    float value15af1;
    float valueMax;

    Car *headcar;
    Car *leavheadcar;
    struct park *nextPark;  
    } Park;

//--------------------AUXILIAR FUNCTIONS-------------------

/// @brief verifies if two str are equal
/// @param name1 
/// @param name2 
/// @return TRUE if the strings are the same FALSE if not 
int striguais(char* name1, char* name2) {
    int i, lim = (int)strlen(name1);
    
    if (lim != (int)strlen(name2)) return 0;
    for (i = 0; i < lim; i++) if (name1[i] != name2[i]) return 0;
    
    return 1;
    }
    

/// @brief verifies if license is valid 
/// @param license 
/// @return TRUE if the license is valid FALSE if not 
int veifLicense(char* license){
    int i;
    char leterspair = 0;    // counter of pairs of letters  
    char numpair = 0;    // counter of pairs of numbers 
    char leterscount = 0;  // count letters in sequence
    char numcount = 0;  // count numbers in sequence
    
    for (i = 0; i < 8 ; i++) {
        if (license[i] == '-') {
            if (leterscount && numcount) return 0;  // if a pair as one number and one letter 
            else {
                if (leterscount) leterspair++; 
                else numpair++;
                leterscount = 0;
                numcount = 0;
                }
            }
        else if ((license[i] >= 'A' && license[i] <= 'Z')) leterscount++;
        else if ((license[i] >= '0' && license[i] <= '9')) numcount++;
        else return 0;    
        }
    if (leterscount && numcount) return 0;  // if a pair as one number and one letter 
    else {
        if (leterscount) leterspair++; 
        else numpair++;
        }
    
    if (!numpair || !leterspair) return 0;
    return 1;
    }

int existPark(Park* headpark, char* name) {
    Park* copyPark;

    if (headpark == NULL) return 0;
    else {
        copyPark = headpark;
        while (copyPark != NULL) {
            if (striguais(copyPark->name, name)) return 1; 
            copyPark = copyPark->nextPark;
            }
        }
    return 0;        
    }

int leapyear(int year) {
    if (!(year%100)) {
        if (!(year%400)) return 1;
        else return 0;
    }
    else if (!(year%4)) return 1;
    else return 0;
}

int verifdate(Date* date) {
    if (    // general cases
        date->min >= 60 
        || date->min < 0 
        || date->hour >= 24 
        || date->hour < 0 
        || date->mon > 12
        || date->mon < 1
        || date->day > 31
        || date->day < 1
        || date->year > 9999
        || date->year < 0
        || ((date->mon == 4 // months with 30 days 
            || date->mon == 6
            || date->mon == 9
            || date->mon == 11)
            && date->day > 30)
        || (date->mon == 2 
            && date->day > 28)
        )
        return 0;
    return 1;
    }


/// @brief writes a park name 
/// @param buffer 
void getname(char* buffer) {
    char c;
    short i = 0, cont = 0;
    short parentheses = 0;    // codition for name with spaces

    while (1) {
        c = getchar();
        if (c == '\n' || c == EOF){
                buffer[i] = '\0'; 
                break;
                }
        if (c == '"' && parentheses) parentheses = 0; // end of parentheses
        else if (c == '"' && !parentheses) parentheses = 1; 
        // ^ start of parentheses
        else if (c == ' ' && !parentheses) {
            cont++; // space count outside of parentheses
            if (cont == 2) {
                buffer[i] = '\0'; // end of name
                break;
                }
            }
        else { 
            buffer[i] = c; 
            i++;
            }
        }
    }


/// @brief frees all the parks in a Park linkes list
/// @param headpark 
void freeall(Park* headpark) {
    Park* temp = headpark;

    if (headpark == NULL) {}
    else {
        while (headpark->nextPark != NULL) {
            temp = headpark->nextPark;
            free(headpark->name);
            free(headpark->headcar);
            free(headpark);
            headpark = temp;
            }
        free(headpark);
        }
    } 

        
/// @brief prints a Park name and free space
/// @param park 
void printparkfreespace(Park* park) {
    printf("%s ",park->name);
    printf("%d\n",park->freespace);
    }


/// @brief verifies if the date is coherent with the last date
/// @param entrydate 
/// @param lastdate 
/// @return TRUE if the date is valid FALSE if not 
int validDate(Date* entrydate, Date* lastdate) {
    long long totalmin;
    long long lastdatemin;
    int tempmon;

    if (lastdate == NULL) return 1;

    totalmin = 
    entrydate->min 
    + (entrydate->hour)*60 
    + (entrydate->day)*MINDAY 
    + entrydate->year*MINYEAR;

    tempmon = entrydate->mon;

    if (tempmon == 1) {}
    else if (tempmon == 2) totalmin += 31*MINDAY;
    else if (tempmon == 3) totalmin += 59*MINDAY;
    else if (tempmon == 4) totalmin += 90*MINDAY;
    else if (tempmon == 5) totalmin += 120*MINDAY;
    else if (tempmon == 6) totalmin += 151*MINDAY;
    else if (tempmon == 7) totalmin += 181*MINDAY;
    else if (tempmon == 8) totalmin += 212*MINDAY;
    else if (tempmon == 9) totalmin += 243*MINDAY;
    else if (tempmon == 10) totalmin += 273*MINDAY;
    else if (tempmon == 11) totalmin += 304*MINDAY;
    else totalmin += 334*MINDAY;
    // ^ adds days of the month in minutes

    lastdatemin = lastdate->min 
    + (lastdate->hour)*60
    + (lastdate->day)*MINDAY
    + lastdate->year*MINYEAR;

    tempmon = lastdate->mon;

    if (tempmon == 1) {}
    else if (tempmon == 2) lastdatemin += 31*MINDAY;
    else if (tempmon == 3) lastdatemin += 59*MINDAY;
    else if (tempmon == 4) lastdatemin += 90*MINDAY;
    else if (tempmon == 5) lastdatemin += 120*MINDAY;
    else if (tempmon == 6) lastdatemin += 151*MINDAY;
    else if (tempmon == 7) lastdatemin += 181*MINDAY;
    else if (tempmon == 8) lastdatemin += 212*MINDAY;
    else if (tempmon == 9) lastdatemin += 243*MINDAY;
    else if (tempmon == 10) lastdatemin += 273*MINDAY;
    else if (tempmon == 11) lastdatemin += 304*MINDAY;
    else lastdatemin += 334*MINDAY;
    // ^ adds days of the month in minutes

    if (lastdatemin > totalmin) return 0;

    return 1;
    }


/// @brief calculats the total facture of a car 
/// @param entrydate 
/// @param leavingdate 
/// @param fee 
/// @param fee1hour 
/// @param specialfee 
/// @return the total amount the car has to pay 
float calcfacture(Date* entrydate, Date* leavingdate, float fee, float fee1hour, float specialfee) {
    float res = 0, 
    total15min, 
    dailyvalue = 4*fee + 92*fee1hour;    // 96 intervales of 15 min a day
    
    int mindiff = leavingdate->min - entrydate->min, 
    hourdiff = (leavingdate->hour - entrydate->hour)*MINHOUR, 
    daydiff = (leavingdate->day - entrydate->day)*MINDAY,
    mondiff = leavingdate->mon - entrydate->mon,    // min calculated next
    yeardiff = (leavingdate->year - entrydate->year)*MINYEAR,
    entrymon = entrydate->mon,
    leavingmon = leavingdate->mon,
    
    i,
    inttotal15min;  //used to verify if   
    
    if (dailyvalue > specialfee) dailyvalue = specialfee;

    if (mondiff == 0) {}
    else if (mondiff > 0) {
        mondiff = 0; // transform the month diff to min
        for (i = entrymon; i < leavingmon; i++) {
            if (i == 4 // months with 30 days 
            || i == 6
            || i == 9
            || i == 11)
                mondiff += 30*MINDAY;
            else if (i == 2) mondiff += 28*MINDAY;
            else mondiff += 31*MINDAY;
            }
        }
    else {
        mondiff = 0; // transform the month diff to min
        for (i = entrymon; i < leavingmon + 12; i++) {
            if (i < 13) {
                if (i == 4 // months with 30 days 
                || i == 6
                || i == 9
                || i == 11)
                    mondiff += 30*MINDAY;
                else if (i == 2) mondiff += 28*MINDAY;
                else mondiff += 31*MINDAY;
                }
            else {
                if (i-12 == 4 // months with 30 days 
                || i-12 == 6
                || i-12 == 9
                || i-12 == 11)
                    mondiff += 30*MINDAY;
                else if (i-12 == 2) mondiff += 28*MINDAY;
                else mondiff += 31*MINDAY;
                }
            }
        mondiff *= -1;
        }
    
    total15min = (mindiff + hourdiff + daydiff + mondiff + yeardiff)/15.0;

    inttotal15min = total15min;

    if (total15min - inttotal15min != 0) total15min = inttotal15min + 1;    
    // ^ round the 15 min up

    while (total15min >= 96) {  
    // if the car is the park more than one day
        res += dailyvalue;
        total15min -= 96;
    }
    if (total15min > 4) {
        if ((total15min - 4)*fee1hour + 4*fee > specialfee) {
            res += specialfee;
            total15min = 0;
            }
        else {
            res += (total15min - 4)*fee1hour;
            total15min = 4;
            }
        }
    if (total15min > 0) {
        if (total15min*fee > specialfee) res += specialfee;
        else res += total15min*fee;
    }

    return res;
    }


/// @brief prints the name and freespace of a Park list
/// @param headpark 
void printparksnames(Park* headpark) {
    Park* temppark = headpark;

    while (temppark != NULL) {
        printf("%s\n",temppark->name);
        temppark = temppark->nextPark;
        }
}


/// @brief substitutes the last date 
/// @param lastdate 
/// @param leavdate 
void subDate(Date* lastdate, Date* leavdate) {
    lastdate->day = leavdate->day;
    lastdate->mon = leavdate->mon; 
    lastdate->year = leavdate->year;
    lastdate->min = leavdate->min;
    lastdate->hour = leavdate->hour;
    }


/// @brief frees a car
/// @param car 
void freeCar(Car* car){
    free(car->license);
    free(car->park);
    free(car->entrydate);
    free(car->leavingdate);
    free(car);
}


/// @brief frees a list of cars 
/// @param headcar 
void freeCars(Car* headcar) {
    Car* next;
    while (headcar != NULL) {
        next = headcar->nextcar;
        freeCar(headcar);
        headcar = next;
    }
}


/// @brief frees all the parks of a Park list
/// @param headpark 
void freeallParks(Park* headpark) {
    Park* tempPark = headpark;
    Park* nextpark;
    while (tempPark != NULL) {
        nextpark = tempPark->nextPark;
        freeCars(tempPark->headcar);
        freeCars(tempPark->leavheadcar);
        free(tempPark->name);
        free(tempPark);
        tempPark = nextpark;
        }

    }


//--------------------FUNCTIONS ABOUT PARKS----------------------


/// @brief prints the parks name, capacity and free space
/// @param park 
void printpark(Park* park) {
        printf("%s ",park->name);
        printf("%d ",park->capac);
        printf("%d\n",park->freespace);
        }


/// @brief prints the names, capacitys and free spaces of a list of parks
/// @param headPark 
void printparks(Park* headPark) {
        Park* copyPark;
        
        if (headPark == NULL) {} 
        else {
                copyPark = headPark;
                while (copyPark->nextPark != NULL) {
                    printpark(copyPark);
                    copyPark = copyPark->nextPark;
                    }
                printpark(copyPark);
                }
        }

/// @brief creates a new park with the input, and verifies the
/// conditions to add it to the park list
/// @param headpark 
/// @param numParks 
/// @param namebuffer 
/// @return the newly created park or a NULL pointer if the
/// conditions are not meet
Park* newpark(Park* headpark, char* numParks, char* namebuffer) {
    Park* ptrPark = malloc(sizeof(Park));
    char* parkname;

    char c;
    int i;  // for buffer index

    short cont = 0;   // space count 
    short parentheses = 2;    // codition for name with spaces
    int decimals = 0;   // condition for decimal places in the fees
    float decimalplacescount = 1;   // to add number in right decimal place
    char negvalue = 0;      // to verify if some fee is negative

    short capacity = 0;
    float fee = 0, fee15min = 0, specialfee = 0;


    for (i = -1; (c = getchar()) != '\n' && c != EOF; i++) {
        
        if (c == '"' && parentheses == 1) {     // when closing parentheses
            parentheses = 0; 
            namebuffer[i-1] = '\0';
            if (existPark(headpark, namebuffer)) {
                printf("%s: parking already exists.\n", namebuffer);
                return NULL;
                }
            }
        else if (c == '"' && parentheses == 2) parentheses = 1;     
        // ^ when opening parentheses
        else if (cont > 1 && c == '-') {
            negvalue = 1;
            break;
            }
        
        else {
            if (c == '.' && !decimals) decimals = 1;
            if (c == ' ' && (parentheses == 2 || parentheses == 0)) {   
            // ^ there are no parentheses opened 
                if (decimals) {decimals = 0; decimalplacescount = 1;}   
                // ^ end of fee ex: 10.12' '<-
                if (parentheses == 2 && cont == 1) {
                    namebuffer[i] = '\0';
                    if (existPark(headpark, namebuffer)) {
                        printf("%s: parking already exists.\n", namebuffer);
                        return NULL;
                        }
                    }
                cont++; 
                }

            else if (c != '.') {
                if (cont == 1) {    // park name
                    if (parentheses == 1) namebuffer[i-1] = c;
                    else namebuffer[i] = c;
                    }   
                else if (cont == 2) capacity = capacity * 10 + c - 48;  // park capacity
                else if (cont == 3) {   // normal park fee
                    if (!decimals) fee = fee * 10 + c - 48;
                    else {decimalplacescount *= 10; fee = fee + (c - 48)/(decimalplacescount);}
                    }  
                else if (cont == 4) {   // fee after 1 hour
                    if (!decimals) fee15min = fee15min * 10 + c - 48;
                    else {decimalplacescount *= 10; fee15min = fee15min + (c - 48)/(decimalplacescount);}
                    }  
                else  {    // special fee
                    if (!decimals) specialfee = specialfee * 10 + c - 48;
                    else{decimalplacescount *= 10; specialfee = specialfee + (c - 48)/(decimalplacescount);}
                    }    
                }
            }
        }

    if (i == -1) {     // if there are no arguments 
        printparks(headpark);
        return NULL;
        }

    else if (*numParks == MAXEST) {
        printf("too many parks.\n"); 
        return NULL;
        }

    else if (capacity <= 0) {
        printf("%d: invalid capacity.\n", capacity); 
        return NULL;
        }

    else if (negvalue
            || fee == 0 
            || fee15min == 0 
            || specialfee == 0 
            || fee > fee15min
            || fee > specialfee
            || fee15min > specialfee
            ) {
            printf("invalid cost.\n");
            return NULL;
            }
  
    else {
        parkname = malloc((strlen(namebuffer) + 1)*sizeof(char));
        strcpy(parkname, namebuffer);
        ptrPark->name = parkname;
        ptrPark->capac = capacity;
        ptrPark->freespace = capacity;
        ptrPark->value15 = fee;
        ptrPark->value15af1 = fee15min;
        ptrPark->valueMax = specialfee;
        ptrPark->headcar = NULL;
        ptrPark->leavheadcar = NULL;
        ptrPark->nextPark = NULL;
    
        return ptrPark;
        }
    }


/// @brief adds a park to the headpark list
/// and increments the number of parks
/// @param headPark 
/// @param numParks 
/// @param namebuffer 
/// @return headpark whit the new park added
Park* addpark(Park* headPark, char* numParks, char* namebuffer) {
    Park* copypark = malloc(sizeof(Park));
    Park* tempPark;
    Park* park;
    char* namecopy;

    park = newpark(headPark, numParks, namebuffer);

    if (park == NULL) {}    
    // ^ if the conditions for the criation of the park are not meet

    else {  // coppying and adding the new park
        namecopy = malloc((strlen(park->name)+1)*sizeof(char));
        strcpy(namecopy,park->name);

        copypark->nextPark = NULL;
        copypark->capac = park->capac;
        copypark->freespace = park->freespace;
        copypark->name = namecopy;
        copypark->headcar = park->headcar;
        copypark->leavheadcar = park->leavheadcar;
        copypark->value15 = park->value15;
        copypark->value15af1 = park->value15af1;
        copypark->valueMax = park->valueMax;

        free(park->name);
        free(park);

        // add the park to the end of the park list
        if (headPark == NULL) headPark = copypark;
        else { 
            tempPark = headPark;
            while (tempPark->nextPark != NULL) tempPark = tempPark->nextPark;
            tempPark->nextPark = copypark;
        }
        (*numParks)++;
    }

    return headPark;
    }


/// @brief adds a park to the list in order according to the ascii table
/// @param headPark head of the list of parks
/// @param park park to add
/// @return returns the list with the new park inserted
Park* addparkorg(Park* headPark, Park* park) {
    Park* copypark = malloc(sizeof(Park));
    Park* tempPark;
    char* namecopy = malloc((strlen(park->name)+1)*sizeof(char));
    
    strcpy(namecopy, park->name); 

    copypark->nextPark = NULL;
    copypark->capac = park->capac;
    copypark->freespace = park->freespace;
    copypark->name = namecopy;
    copypark->headcar = park->headcar;
    copypark->leavheadcar = park->leavheadcar;
    copypark->value15 = park->value15;
    copypark->value15af1 = park->value15af1;
    copypark->valueMax = park->valueMax;

    if (headPark == NULL) {
        headPark = copypark;
        }
    else if (strcmp(copypark->name, headPark->name) < 0) {  
    // ^ if the new park should be placed before the first park in the list
        copypark->nextPark = headPark;
        return copypark;       
        }
    else {
        tempPark = headPark;
        while (tempPark->nextPark != NULL) {
            if (strcmp(copypark->name, (tempPark->nextPark)->name) < 0) {
            // ^ if the new park should be placed after tempPark
                copypark->nextPark = tempPark->nextPark;
                tempPark->nextPark = copypark;
                break;
                }
            else tempPark = tempPark->nextPark;
            }
        if (tempPark->nextPark == NULL) tempPark->nextPark = copypark;
        }

    return headPark;        
    }
    
/// @brief creats a new list with the elements of headpark list organized
/// @param headpark fist elemente of the list
/// @return Park with the elements of headpark list organized
Park* orgparks(Park* headpark) {
    Park* NewPark = NULL;
    Park* copypark = headpark;

    while (copypark != NULL) {
        NewPark = addparkorg(NewPark, copypark);
        copypark = copypark->nextPark;
    }
    return NewPark;
}

/// @brief prints the facture of a park or 
/// the facture of a park in a specific date (if the date is valid)
/// @param headpark 
/// @param lastdate last entry
/// @return nothing
int parkfact(Park* headpark, Date* lastdate) {
    Date* date = malloc(sizeof(Date));
    Park* temppark = headpark;
    Car* headCar;
    
    char* buffer = malloc(MAXLINE*sizeof(char));
    
    char c;
    char conthyphen = 0;    // to identify what part of the date is being written
    short i;
    
    short year = 0, mon = 0, day = 0;
    float fact = 0;
    short cont = 0;     // space count
    short parentheses = 2;    // codition for name with spaces
    
    date->min = 0;  // default times
    date->hour = 0;

    c = getchar();  // for the space after 'f'

    for (i = 0; (c = getchar()) != '\n' && c != EOF; i++) {
        if (cont < 1) {
            if (c == '"' && parentheses == 1) parentheses = 0;  // to open parentheses
            else if (c == '"' && parentheses != 1) parentheses = 1;  // to close parentheses
            else if (c == ' ' && parentheses != 1) {    
                cont++;
                if (cont == 1) {
                    buffer[i] = '\0';   // end park name 
                    } 
                }
            else { 
                if (parentheses == 1) buffer[i-1] = c; 
                else buffer[i] = c; 
                }
            }
        else {
            if (c == '-') conthyphen++;
            else if (c == ' ') {}
            else if (!conthyphen) day = day * 10 + c - 48;  
            else if (conthyphen == 1) mon = mon * 10 + c - 48;  
            else year = year * 10 + c - 48;  
            } 
        }


    date->day = day;
    date->mon = mon;
    date->year = year;

    if (year == 0) {   // one argument 
        
        while (!striguais(temppark->name, buffer)) { 
        // ^ verify if the park exists
            if (temppark->nextPark == NULL) {
                printf("%s: no such parking.\n",buffer);
                free(buffer);                 
                return 1;
                }
            temppark = temppark->nextPark;
            }
        headCar = temppark->leavheadcar;
        while (headCar != NULL) {
            if (year == 0) {    // year is 0 in the first cycle
                year = (headCar->leavingdate)->year;
                mon = (headCar->leavingdate)->mon;
                day = (headCar->leavingdate)->day;
                }
            if (year != (headCar->leavingdate)->year 
                || mon != (headCar->leavingdate)->mon 
                || day != (headCar->leavingdate)->day) { 
                // ^ if after a cycle the day is not the same, print the 
                // accumulated value of the facture of the day and atualize the date
                printf("%02d-%02d-%04d %.2f\n", day, mon, year, fact);
                fact = 0;
                year = (headCar->leavingdate)->year;
                mon = (headCar->leavingdate)->mon;
                day = (headCar->leavingdate)->day;
                }
            fact += calcfacture(headCar->entrydate, 
                                headCar->leavingdate, 
                                temppark->value15, 
                                temppark->value15af1, 
                                temppark->valueMax);
            // ^ add to the facture
            headCar = headCar->nextcar;
            }
        if (fact != 0) printf("%02d-%02d-%04d %.2f\n", day, mon, year, fact);
        // ^ print the facture of the last day 
        }
    else {  // specific date 
        
        while (!striguais(temppark->name, buffer)) {
        // ^ verify if the park exists
            if (temppark->nextPark == NULL) {
                printf("%s: no such parking.\n",buffer); 
                free(buffer);
                return 1;
                }
            temppark = temppark->nextPark;
            }
        headCar = temppark->leavheadcar;
        if (!verifdate(date) || validDate(date, lastdate)) {
            printf("invalid date.\n"); 
            free(buffer);
            return 1;
            }
        while (headCar != NULL) {
            if (year == (headCar->leavingdate)->year 
                && mon == (headCar->leavingdate)->mon 
                && day == (headCar->leavingdate)->day) {
            // ^ if the car left that date print facture
                fact = calcfacture(headCar->entrydate, 
                                headCar->leavingdate, 
                                temppark->value15, 
                                temppark->value15af1, 
                                temppark->valueMax);
                printf("%s %02d:%02d %.2f\n", headCar->license, (headCar->leavingdate)->hour, (headCar->leavingdate)->min, fact);
                }
            headCar = headCar->nextcar;
            }
        }  
    return 1;
    }
    
/// @brief removes a park and all its car entries 
/// @param headpark 
/// @param numParks 
/// @param strbuffer 
/// @return a Park list without the patk removed
Park* removepark(Park* headpark, char* numParks, char* strbuffer) {
    Park* temppark = headpark;
    Park* parktoremove = NULL;
    char* namecopy;

    getname(strbuffer);

    namecopy = malloc((strlen(strbuffer)+1)*sizeof(char));
    strcpy(namecopy, strbuffer);

    if (headpark == NULL) {
        printf("%s: no such parking.\n", namecopy);
        return headpark;
        }
    else if (striguais(namecopy, headpark->name)) {
    // ^ if the first park is the park to remove
        parktoremove = headpark;
        headpark = headpark->nextPark;
        }
    else {
        while (temppark->nextPark != NULL) {
            if (striguais(namecopy, (temppark->nextPark)->name)) {
            // if the park to remove is the park next to temppark
                parktoremove = temppark->nextPark; 
                temppark->nextPark = parktoremove->nextPark;
                break;
                }
            temppark = temppark->nextPark;
            } 
        }

    if (parktoremove == NULL) {
    // ^ if the park list ends and the park to remove is not foud
        printf("%s: no such parking.\n", namecopy);
        return headpark;
        }

    freeCars(parktoremove->headcar);
    freeCars(parktoremove->leavheadcar);
    free(parktoremove->name);
    free(parktoremove);
    free(namecopy);

    printparksnames(orgparks(headpark));
    
    (*numParks)--;
    return headpark;
}


//-------------------FUNCTIONS ABOUT CARS----------------------


/// @brief adds a car to a linked list of cars 
/// @param headcar 
/// @param car 
/// @return the new link list 
Car* addcar(Car* headcar, Car* car) {   // for car linkedlist  

    Car* copycar = (Car*)malloc(sizeof(Car));
    char* licence = malloc(sizeof(char)*(LICENSESIZE+1));
    char* name;
    Car* tempcar;
    Date* entrydate = (Date*)malloc(sizeof(Date));
    Date* leavdate;

    if (car == NULL) return headcar; 
    strcpy(licence, car->license);

    name = malloc(sizeof(char)*(strlen(car->park)+1));
    strcpy(name, car->park);

    copycar->license = licence;
    copycar->park = name;
    
    entrydate->day = (car->entrydate)->day;
    entrydate->mon = (car->entrydate)->mon;
    entrydate->year = (car->entrydate)->year;
    entrydate->min = (car->entrydate)->min;
    entrydate->hour = (car->entrydate)->hour;

    if (car->leavingdate != NULL) {
        leavdate = (Date*)malloc(sizeof(Date));
        leavdate->day = (car->leavingdate)->day;
        leavdate->mon = (car->leavingdate)->mon;
        leavdate->year = (car->leavingdate)->year;
        leavdate->min = (car->leavingdate)->min;
        leavdate->hour = (car->leavingdate)->hour;
        }
    else leavdate = NULL;

    copycar->entrydate = entrydate;
    copycar->nextcar = NULL;
    copycar->leavingdate = leavdate;

    if (headcar == NULL) {
        headcar = copycar;
        }
    else {
        tempcar = headcar;
        while (tempcar->nextcar != NULL) tempcar = tempcar->nextcar;
        tempcar->nextcar = copycar;
        }


    return headcar;        
    }
    

/// @brief verifies if the car with the license 'license' is any park
/// @param headpark 
/// @param license 
/// @return returns TRUE if the car is in any park and false if it isnt
int Carinparks(Park* headpark, char* license) {  
    Park* tempPark = headpark;
    Car* tempCar;

    while (tempPark != NULL) {
        tempCar = tempPark->headcar;
        while (tempCar != NULL) {
            if (striguais(tempCar->license, license) && tempCar->leavingdate == NULL) return 1;
            tempCar = tempCar->nextcar;
            }
        tempPark = tempPark->nextPark;
        }

    return 0;
    }


/// @brief verifies if the car with the license 'license' is a specific park
/// @param park 
/// @param license 
/// @return returns TRUE if the car is in the park and false if it isnt
int Carinpark(Park* park, char* license) {  // verifies if the car is or was in the park
    Car* tempCar = park->headcar;
    
    while (tempCar != NULL) {
        if (striguais(tempCar->license, license)) return 1;
        tempCar = tempCar->nextcar;
        }

    return 0;
    }


/// @brief creates a new car with the input given and adds it
/// to the specified park, also verifies the exeptions
/// @param headpark 
/// @param lastdate 
/// @param name 
/// @return pointer to a park
Park* newcar(Park* headpark, Date* lastdate, char* name) {
    Park* copypark;
    Date* date = (Date*)malloc(sizeof(Date));
    Car* ptrCar = (Car*)malloc(sizeof(Car));
    
    char* license = (char*)malloc(sizeof(char)*(LICENSESIZE+1));
    char* namecopy;

    char c;
    int i;  // for buffer index
    
    char cont = 0;   // to count spaces
    char conthyphen = 0;    // to distinguish betwin day,month and year
    char cont2points = 0;   // to distinguish betwin min and hour
    
    short year = 0, month = 0, day = 0, hour = 0, min = 0;

    if (headpark == NULL) {
        printf("%s: no such parking.\n", name);
        free(ptrCar);
        free(license);
        free(date);
        return headpark;
        }

    getname(name);
    
    copypark = headpark;
    while (copypark != NULL) {
        if (striguais(copypark->name, name)) break; 
        copypark = copypark->nextPark;
        }
    if (copypark == NULL) {
        printf("%s: no such parking.\n", name);
        free(ptrCar);
        free(license);
        free(date);
        return headpark;
        }

    if (copypark->freespace == 0) {  
        printf("%s: parking is full.\n", name);
        free(ptrCar);
        free(license);
        free(date);
        return headpark;
        } 

    namecopy = malloc((strlen(name) + 1)*sizeof(char));     // space for '\0' 
    strcpy(namecopy, name);

    for (i = 0; (c = getchar()) != '\n' && c != EOF; i++) {
        
        if (c == '-' && cont == 1) conthyphen++;
        else if (c == ':' && cont == 2) cont2points++;

        else {
            if (c == ' ') {
                if (cont == 0) license[i] = '\0';
                cont++;
                }

            else {
                if (cont == 0) {   // license
                    license[i] = c;
                    }  
                else if (cont == 1) {   // date
                    if (!conthyphen) day = day * 10 + c - 48;  
                    else if (conthyphen == 1) month = month * 10 + c - 48;  
                    else year = year * 10 + c - 48;  
                    }  
                else if (cont == 2) {   // hours
                    if (!cont2points) hour = hour * 10 + c - 48;  
                    else if (cont2points) min = min * 10 + c - 48;  
                    }  
                }
            }
        }

    if (!veifLicense(license)) {
        printf("%s: invalid licence plate.\n", license);
        free(ptrCar);
        free(license);
        free(date);
        return headpark;
        }
    
    ptrCar->license = license;
    ptrCar->park = namecopy;

    date->day = day;
    date->mon = month;
    date->year = year;
    date->hour = hour;
    date->min = min;

    if (!verifdate(date)) {    // only verifies if the date is valid
        printf("invalid date.\n");
        free(ptrCar);
        free(license);
        free(date);
        return headpark;
        }
    if (!validDate(date, lastdate)) {     // verifies if the time line is coherent 
        printf("invalid date.\n");
        free(ptrCar);
        free(license);
        free(date);
        return headpark;
        }

    ptrCar->entrydate = date;
    ptrCar->leavingdate = NULL; // default
    ptrCar->nextcar = NULL; // default

    if (Carinparks(headpark, license)) {
    printf("%s: invalid vehicle entry.\n", license);
    free(ptrCar);
    free(license);
    free(date);
    return headpark;
    }
    
    while (!striguais(copypark->name, namecopy)) copypark = copypark->nextPark;
    copypark->headcar = addcar(copypark->headcar, ptrCar);
    
    copypark->freespace = copypark->freespace - 1;
    printparkfreespace(copypark);
    subDate(lastdate, date);
    return headpark;
    }


/// @brief verifies if the car is or was in any park
/// @param headpark 
/// @param license 
/// @return TRUE if the car is or was FALSE if the contrary 
int existCar(Park* headpark, char* license) {   
    Park* tempPark = headpark;
    Car* tempCar;

    while (tempPark != NULL) {
        tempCar = tempPark->headcar;
        while (tempCar != NULL) {
            if (striguais(tempCar->license, license)) return 1;
            tempCar = tempCar->nextcar;
            }
        tempPark = tempPark->nextPark;
    }

    return 0;
    }

        
/// @brief removes a car from a specific park and 
/// verifies if the input is correct
/// @param headpark 
/// @param lastdate 
/// @param strbuffer 
/// @return irrelevant
int removecar(Park* headpark, Date* lastdate, char* strbuffer) {
    Park* copypark = headpark;
    Car* tempcar;
    Date* leavdate = malloc(sizeof(Date));

    char* templicense = malloc((LICENSESIZE+1)*sizeof(char));

    char c, 
    cont = 0;   //to indentify what is being written 
    short i;    // index for buffer
    char conthyphen = 0, cont2points = 0;

    short year = 0, month = 0, day = 0, hour = 0, min = 0;
    float fact;

    getname(strbuffer);

    if (!existPark(headpark, strbuffer)) {
            printf("%s: no such parking.\n", strbuffer);
            free(templicense);
            return 0;
            }
    else {
        scanf("%s", templicense);
        c = getchar();  // for space after
        if (!veifLicense(templicense)) {
            printf("%s: invalid licence plate.\n", templicense);
            free(templicense);
            return 0;
            }
        }
    
    for (i = 0; (c = getchar()) != '\n' && c != EOF; i++) {

        if (c == '-' && cont == 0) conthyphen++;
        else if (c == ':' && cont == 1) cont2points++;

        else if (c == ' ') cont++;
        else {
            if (cont == 0) {   // date
                if (!conthyphen) day = day * 10 + c - 48;  
                else if (conthyphen == 1) month = month * 10 + c - 48;  
                else year = year * 10 + c - 48;  
                }  
            else if (cont == 1) {   // hours
                if (!cont2points) hour = hour * 10 + c - 48;  
                else if (cont2points) min = min * 10 + c - 48;  
                }
            }  
        }

    leavdate->min = min;
    leavdate->hour = hour;
    leavdate->day = day;
    leavdate->mon = month;
    leavdate->year = year;

    if (!verifdate(leavdate) || !validDate(leavdate, lastdate)) {
        printf("invalid date.\n"); 
        free(templicense);
        return 0;
        }

    while (!striguais(copypark->name, strbuffer)) 
        copypark = copypark->nextPark;

    tempcar = copypark->headcar;
    if (tempcar == NULL) {
        printf("%s: invalid vehicle exit.\n", templicense);
        free(templicense);
        return 0;
        }
    while (!striguais(tempcar->license, templicense) || tempcar->leavingdate != NULL) {
        if (tempcar->nextcar == NULL) { 
            printf("%s: invalid vehicle exit.\n", templicense); 
            free(templicense);
            return 0;
            }
        tempcar = tempcar->nextcar;
        }

    tempcar->leavingdate = leavdate;    
    copypark->freespace++;  // increses park free spaces
    copypark->leavheadcar = addcar(copypark->leavheadcar, tempcar); 
    // ^ adds car to the list of cars that have left the park
        
    fact = calcfacture(tempcar->entrydate, leavdate, copypark->value15, copypark->value15af1, copypark->valueMax);

    printf("%s %02d-%02d-%02d %02d:%02d %02d-%02d-%02d %02d:%02d %.2f\n",
            templicense,
            (tempcar->entrydate)->day,
            (tempcar->entrydate)->mon,
            (tempcar->entrydate)->year, 
            (tempcar->entrydate)->hour,
            (tempcar->entrydate)->min, 
            leavdate->day, 
            leavdate->mon, 
            leavdate->year, 
            leavdate->hour, 
            leavdate->min,
            fact
            );  // prints cars entry and leaving date facture

    if (leavdate != NULL) subDate(lastdate, leavdate);

    free(templicense);

    return 0;
    }


/// @brief prints all the cars entries of a specific car
/// also validates the input
/// @param headPark 
/// @return irrelevent
int carentries(Park* headPark) {
    Park* tempPark;
    Car* tempCar;
    char* license = malloc((LICENSESIZE+1)*sizeof(char));
    
    getchar();  // for the space after 'v'
    scanf("%s", license);

    if (!veifLicense(license)) {
        printf("%s: invalid licence plate.\n", license);
        return 0;
        }
    else if (!existCar(headPark, license)) {
        printf("%s: no entries found in any parking.\n", license);
        return 0;
        }

    tempPark = orgparks(headPark);

    while (tempPark != NULL) {
        if (Carinpark(tempPark, license)) { 
        // ^ if the car is or was in this park print the entry (and leaving date)
            tempCar = tempPark->headcar;
            while (tempCar != NULL) {
                if (striguais(tempCar->license, license)) {
                    if (tempCar->leavingdate == NULL)
                    printf("%s %02d-%02d-%02d %02d:%02d\n",
                    tempPark->name,
                    (tempCar->entrydate)->day,
                    (tempCar->entrydate)->mon,
                    (tempCar->entrydate)->year, 
                    (tempCar->entrydate)->hour,
                    (tempCar->entrydate)->min
                    );
                    else 
                    printf("%s %02d-%02d-%02d %02d:%02d %02d-%02d-%02d %02d:%02d\n",
                    tempPark->name,
                    (tempCar->entrydate)->day,
                    (tempCar->entrydate)->mon,
                    (tempCar->entrydate)->year, 
                    (tempCar->entrydate)->hour,
                    (tempCar->entrydate)->min, 
                    (tempCar->leavingdate)->day, 
                    (tempCar->leavingdate)->mon, 
                    (tempCar->leavingdate)->year, 
                    (tempCar->leavingdate)->hour, 
                    (tempCar->leavingdate)->min
                    );
                    }
                tempCar = tempCar->nextcar;
                }
                    
                }
        tempPark = tempPark->nextPark;
        }
    
    free(license);
    return 0;
    }



