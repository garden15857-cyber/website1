from myapp import create_app

app = create_app()

if __name__ == '__main__':
    print("✅ Server start")
    app.run(host='0.0.0.0', port=10000)