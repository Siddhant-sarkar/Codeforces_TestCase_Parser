# Codeforces TestCases Parser 
> Due to ❤️ of codeforces.

* This extension helps the sublime text users to easily copy their problems's 
testcases very quickly into a file named **`inputf.in`**
* the test case are of the form :

```
N
test_case1

test_case2
.
.
.
.
.
test_caseN
```

* Be sure to take **extra care** for different test cases as you have to switch on and off the loop __while submiting your answer__.
```C++
int t ; 
cin >> t; // <-- take extra care here.
while(t--){
  // the function to solve the equation 
  solve();
}
```


* if you want to change the inputfile name you can do so by 
```Python
 k = os.path.split(filename)[0] +'/inputf.in'
 # By simply changing the name to /{your_file_name_here}
```
## Made with ❤️ wish that i become master on Codeforces soon 🥳 .





