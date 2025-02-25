backend app api run ----------> uvicorn app:app --reload

App will be live at: http://127.0.0.1:8000

Endpoints:

1. /run-code
   Sample input:
   {
   "language": "java",
   "code": "\npublic class Main {\n\tpublic static void main(String[] args) {\n\t\tint number = 6; // Setting n = 6\n long result = factorial(number);\n System.out.println(\"Factorial of \" + number + \" is: \" + result);\n }\n\n public static long factorial(int n) {\n long result = 1;\n for (int i = 1; i <= n; i++) {\n result \*= i;\n }\n return result;\n }\n}\n"
   }

2. /generate-code
   Sample input:
   {
   "prompt": "Wrtie a prohram to find power of x to n in java."
   }
