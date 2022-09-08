from main import main
import glob

my_path=  './tests'
files = glob.glob(my_path + '/**/*.txt', recursive=True)
print(files)
for file in files:
    print(file)
    main(file)