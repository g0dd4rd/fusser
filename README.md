# fusser
- simple fuzzer
- usage: string-generator.py <program> <program arguments> <options> <arguments>
- [x] -h           prints this help
- [x] -p           generate only the printable ASCII characters
- [x] -a           generate all ASCII characters
- [x] -0           include the null (0 byte) character
- [x] -n           generate only digits
- [x] -l <range>   generate random length lines within <range> (\n terminated strings)
- [x] -f <name>    record characters in file <name>
- [x] -d <seconds> waits <seconds> following each character
- [x] -r <name>    replay characters in file <name> to output

