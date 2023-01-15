from classs import create_class

def main():
    app = create_class()
    print(app.get("/"))

if __name__ == "__main__":
    main()
