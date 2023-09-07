YOUR NO FUSS BIKE SHARING APP 


TO DO:
-configure bike registry so that it has a relationship to bike owners
-configure the bike session table to register bike borrows, borrow session will be time stamped, and deduct fees at x rate if not returned, or for regular tune up if bike is not in proper condition.
-set up a window in home page to show registered bikes and borrowed bikes

App for lending library of bikes.

WHAT - This projct uses Python, Bootstrap, SQLAlchemy, Flask, (and Jinja???)

HOW - One database, 3 Class Object Oriented Program

    THIS PROJECT IS USING BOOTSTRAP, SQLALCHEMY, AND FLASK
    TEMPLATES - HOLD HTML FILES

    STATIC - TAKES JS, OR IMAGES, OR CSS, ONCE THEY ARE SAVED IN THE DIRECTORY, YOU CAN LOAD THEM IN THE HTML WITH THE FOLLOWING PROTOTYPE: 
        <script>
        type="text/javascript"
        src="{{  url_for('static'), filename='index.js')  }}"
        </script>
    

    -base.html IS THE TEMPLATE, TO USE THE TEMPLATE, YOU ~EXTEND~ THE TEMPLATE WITH BLOCK CURLY BRACKETS
         IE: {% block title %}  {% endblock %}
    -TO RENDER, CONFIGURE IN views.py file (YOUR DIRECTORY) ONCE THE base.html IS DEFINED, IMPORT render_template, AND USE THE FOLLOWING CLASS METHOD SYNTAX:

        @views.route('/)
        def home():
        return render_template("home.html")

        OR

        @auth.route('login.html')
        def login():
        return render_tenmplate("login.html")

    
    -TO PASS VARIABLES INTO YOUR TEMPLATE, YOU USE {{ }}
        THIS WRAPS A PYTHON EXPRESSION INSIDE, AND INTERPOLATES ANY TEXT YOU DEFINED IN YOUR VARIABLE THAT LIVES IN ITS RESPECTIVE CLASS METHOD:
            IE:         @auth.route('login.html')
                        def login():
                        return render_tenmplate("login.html", text="TESTING)

                        ^^ variable text is defined, and then interpolated in login file like so {{ text }}

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



