from theFormForaccepted import create_app

app =  create_app()



# kick out

if __name__ == "__main__":
    app.run(debug=True, port=8080)