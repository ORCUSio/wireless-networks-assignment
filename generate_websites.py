import os

def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

# ==========================================
# Q8: College Website Generator
# ==========================================
base_dir_q8 = "Q8_CollegeWebsite"
if not os.path.exists(base_dir_q8):
    os.makedirs(base_dir_q8)

style_q8 = """
    <style>
        body { font-family: Arial, sans-serif; background-color: #f0f8ff; margin: 0; padding: 0; }
        header { background-color: #003366; color: white; padding: 20px; text-align: center; }
        nav { background-color: #004080; padding: 10px; text-align: center; }
        nav a { color: white; margin: 0 15px; text-decoration: none; font-weight: bold; }
        nav a:hover { text-decoration: underline; }
        .container { padding: 20px; max-width: 900px; margin: auto; background-color: white; min-height: 400px; border-left: 1px solid #ddd; border-right: 1px solid #ddd; }
        footer { background-color: #003366; color: white; text-align: center; padding: 10px; position: relative; bottom: 0; width: 100%; margin-top: 20px; }
        h1, h2 { color: #003366; }
        table { border-collapse: collapse; width: 100%; margin-top: 20px; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #003366; color: white; }
        .gallery img { width: 300px; height: 200px; margin: 10px; border: 5px solid #ddd; }
        /* Logo Placeholder */
        .logo { width: 80px; height: 80px; vertical-align: middle; margin-right: 10px; }
    </style>
"""

header_q8 = """
    <header>
        <img src="https://via.placeholder.com/80?text=Logo" alt="College Logo" class="logo">
        <span style="font-size: 2em; vertical-align: middle;">Grand Institute of Technology</span>
    </header>
    <nav>
        <a href="index.html">Home</a>
        <a href="academics.html">Academics</a>
        <a href="admission.html">Admission</a>
        <a href="gallery.html">Gallery</a>
        <a href="about.html">About Us</a>
        <a href="contact.html">Contact</a>
    </nav>
"""

footer_q8 = """
    <footer>
        &copy; 2026 Grand Institute of Technology. All Rights Reserved.
    </footer>
"""

def create_page_q8(filename, title, body_content):
    content = f"""<!DOCTYPE html>
<html>
<head>
    <title>{title} - Grand Institute of Technology</title>
    {style_q8}
</head>
<body>
    {header_q8}
    <div class="container">
        <h2>{title}</h2>
        {body_content}
    </div>
    {footer_q8}
</body>
</html>"""
    write_file(os.path.join(base_dir_q8, filename), content)

# 1. Home Page
create_page_q8("index.html", "Welcome to GIT", """
    <p>Welcome to the Grand Institute of Technology (GIT). We are dedicated to providing world-class education in Arts, Science, and Commerce.</p>
    <p>Our campus is equipped with state-of-the-art facilities, expanding over 50 acres of lush green land.</p>
    <img src="https://via.placeholder.com/800x300?text=College+Campus" style="width:100%; border-radius: 5px;">
""")

# 2. Academics Page (Nested List)
courses = {
    "Science": ["Computer Science", "Mathematics", "Physics"],
    "Arts": ["English", "Sociology", "History"],
    "Commerce": ["Accountancy", "Economics", "Business Studies"]
}

academics_html = "<ul>"
for dept, subjects in courses.items():
    academics_html += f"<li><strong>{dept}</strong><ul>"
    for subj in subjects:
        slug = f"{dept.lower()}_{subj.lower().replace(' ', '_')}.html"
        academics_html += f'<li><a href="{slug}">{subj}</a></li>'
    academics_html += "</ul></li>"
academics_html += "</ul>"

create_page_q8("academics.html", "Academics", f"""
    <p>Our college offers a wide range of courses across various disciplines.</p>
    {academics_html}
""")

# 3. Admission Page (Form)
create_page_q8("admission.html", "Admission Form", """
    <form action="#" method="post">
        <label>Full Name:</label><br>
        <input type="text" name="name" required style="width: 300px;"><br><br>
        
        <label>Email:</label><br>
        <input type="email" name="email" required style="width: 300px;"><br><br>
        
        <label>Phone:</label><br>
        <input type="text" name="phone" required style="width: 300px;"><br><br>
        
        <label>Course Interested:</label><br>
        <select name="course" style="width: 310px;">
            <option>Computer Science</option>
            <option>Mathematics</option>
            <option>English</option>
            <option>Accountancy</option>
        </select><br><br>
        
        <label>Gender:</label><br>
        <input type="radio" name="gender" value="Male"> Male
        <input type="radio" name="gender" value="Female"> Female<br><br>
        
        <label>Address:</label><br>
        <textarea name="address" rows="4" style="width: 300px;"></textarea><br><br>
        
        <input type="submit" value="Submit Application">
    </form>
""")

# 4. Gallery Page
create_page_q8("gallery.html", "Photo Gallery", """
    <div class="gallery">
        <img src="https://via.placeholder.com/300x200?text=Students" alt="Students">
        <img src="https://via.placeholder.com/300x200?text=Library" alt="Library">
        <img src="https://via.placeholder.com/300x200?text=Lab" alt="Lab">
        <img src="https://via.placeholder.com/300x200?text=Sports" alt="Sports">
        <img src="https://via.placeholder.com/300x200?text=Classroom" alt="Classroom">
        <img src="https://via.placeholder.com/300x200?text=Event" alt="Event">
    </div>
""")

# 5. About Page
create_page_q8("about.html", "About Us", """
    <p>Established in 1990, GIT has been a pioneer in education...</p>
""")

# 6. Contact Page
create_page_q8("contact.html", "Contact Us", """
    <p>Email: info@git.edu</p>
    <p>Phone: +91 12345 67890</p>
    <p>Address: 123 Knowledge Park, Education City.</p>
""")

# Generate Course Pages (9 pages)
for dept, subjects in courses.items():
    for subj in subjects:
        slug = f"{dept.lower()}_{subj.lower().replace(' ', '_')}.html"
        body = f"""
            <p>Welcome to the Department of {dept}. This is the dedicated page for the <strong>{subj}</strong> course.</p>
            <h3>Course Description</h3>
            <p>This course provides in-depth knowledge and practical skills in {subj}.</p>
            <h3>Faculty</h3>
            <ul>
                <li>Dr. A. Sharma - Professor</li>
                <li>Mr. B. Singh - Assistant Professor</li>
            </ul>
            <h3>Timetable</h3>
            <table>
                <tr><th>Day</th><th>Time</th><th>Subject</th></tr>
                <tr><td>Monday</td><td>10:00 AM</td><td>{subj} Theory</td></tr>
                <tr><td>Wednesday</td><td>02:00 PM</td><td>{subj} Lab</td></tr>
                <tr><td>Friday</td><td>11:00 AM</td><td>{subj} Tutorial</td></tr>
            </table>
        """
        create_page_q8(slug, f"{subj} - {dept}", body)

# Total Pages Q8: 6 + 9 = 15. Perfect.


# ==========================================
# Q9: Tourism Website Generator
# ==========================================
base_dir_q9 = "Q9_TourismWebsite"
if not os.path.exists(base_dir_q9):
    os.makedirs(base_dir_q9)

style_q9 = """
    <style>
        body { font-family: 'Georgia', serif; background-color: #fffaf0; margin: 0; padding: 0; }
        header { background-color: #8b4513; color: white; padding: 20px; text-align: center; }
        nav { background-color: #a0522d; padding: 10px; text-align: center; }
        nav a { color: white; margin: 0 15px; text-decoration: none; font-size: 1.1em; }
        nav a:hover { text-decoration: underline; color: #ffd700; }
        .container { padding: 40px; max-width: 1000px; margin: auto; background-color: white; box-shadow: 0 0 10px rgba(0,0,0,0.1); min-height: 500px; }
        footer { background-color: #8b4513; color: white; text-align: center; padding: 20px; margin-top: 40px; }
        h1, h2, h3 { color: #8b4513; }
        .heritage-list { display: flex; flex-wrap: wrap; justify-content: space-around; }
        .heritage-item { margin: 15px; text-align: center; border: 1px solid #ccc; padding: 10px; border-radius: 8px; transition: transform 0.2s; }
        .heritage-item:hover { transform: scale(1.05); box-shadow: 0 5px 15px rgba(0,0,0,0.2); }
        .heritage-item img { width: 200px; height: 150px; object-fit: cover; border-radius: 5px; }
        .heritage-item a { display: block; margin-top: 10px; text-decoration: none; color: #8b4513; font-weight: bold; background-color: #fcebb6; padding: 5px; border-radius: 4px; }
        .form-group { margin-bottom: 15px; }
        label { display: block; margin-bottom: 5px; font-weight: bold; }
        input, select, textarea { width: 100%; padding: 8px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; }
        button { background-color: #8b4513; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer; }
        button:hover { background-color: #a0522d; }
    </style>
"""

header_q9 = """
    <header>
        <h1>Visit Historic City</h1>
        <p>Experience the Culture and Heritage</p>
    </header>
    <nav>
        <a href="index.html">Home</a>
        <a href="heritage.html">Heritage Sites</a>
        <a href="hotel_booking.html">Hotel Booking</a>
        <a href="gallery.html">Gallery</a>
        <a href="contact.html">Contact</a>
    </nav>
"""

footer_q9 = """
    <footer>
        &copy; 2026 City Tourism Board. Plan your trip today!
    </footer>
"""

def create_page_q9(filename, title, body_content):
    content = f"""<!DOCTYPE html>
<html>
<head>
    <title>{title} - City Tourism</title>
    {style_q9}
</head>
<body>
    {header_q9}
    <div class="container">
        <h2>{title}</h2>
        {body_content}
    </div>
    {footer_q9}
</body>
</html>"""
    write_file(os.path.join(base_dir_q9, filename), content)

# Sites Data
sites = [
    ("Old Fort", "A massive fort built in the 16th century, offering panoramic views of the city.", "16th Century"),
    ("Royal Palace", "The residence of the royal family, featuring exquisite architecture and museums.", "18th Century"),
    ("City Museum", "Housing artifacts and relics from the city's glorious past.", "19th Century"),
    ("Botanical Garden", "A lush green garden with rare species of plants and flowers.", "1920"),
    ("Sunset Point", "A scenic hilltop offering breathtaking views of the sunset.", "Natural"),
    ("Ancient Temple", "A spiritual center famous for its intricate stone carvings.", "10th Century"),
    ("Market Square", "The bustling heart of the city, famous for handicrafts and street food.", "Traditional"),
    ("Clock Tower", "An iconic landmark standing tall in the city center.", "1880"),
    ("Riverfront", "A peaceful promenade along the holy river.", "Modern renovation"),
    ("War Memorial", "Dedicated to the brave soldiers who laid down their lives.", "1950")
]

# 1. Home
create_page_q9("index.html", "Welcome to the City", """
    <p>Welcome to our beautiful city, a place where history comes alive. Explore our magnificent forts, palaces, and vibrant culture.</p>
    <img src="https://via.placeholder.com/900x400?text=City+Panorama" style="width:100%; border-radius: 8px;">
""")

# 2. Heritage Page (List of 10)
heritage_html = '<div class="heritage-list">'
for i, (name, desc, _) in enumerate(sites):
    slug = f"site_{i+1}.html"
    heritage_html += f"""
        <div class="heritage-item">
            <img src="https://via.placeholder.com/200x150?text={name.replace(' ', '+')}" alt="{name}">
            <h3>{name}</h3>
            <a href="{slug}">View Details</a>
        </div>
    """
heritage_html += '</div>'

create_page_q9("heritage.html", "Heritage Sites", f"""
    <p>Discover the top attractions of our city. Click on any site to learn more.</p>
    {heritage_html}
""")

# 3. Hotel Booking
create_page_q9("hotel_booking.html", "Hotel Booking", """
    <form action="#" method="post">
        <div class="form-group">
            <label>Name:</label>
            <input type="text" name="name" required>
        </div>
        <div class="form-group">
            <label>Check-in Date:</label>
            <input type="date" name="checkin" required>
        </div>
        <div class="form-group">
            <label>Check-out Date:</label>
            <input type="date" name="checkout" required>
        </div>
        <div class="form-group">
            <label>Number of Guests:</label>
            <input type="number" name="guests" min="1" value="1">
        </div>
        <div class="form-group">
            <label>Room Type:</label>
            <select name="room_type">
                <option>Standard</option>
                <option>Deluxe</option>
                <option>Suite</option>
            </select>
        </div>
        <button type="submit">Book Now</button>
    </form>
""")

# 4. Gallery
gallery_html = '<div class="heritage-list">'
for name, _, _ in sites:
    gallery_html += f"""
        <div class="heritage-item" style="border:none; box-shadow:none;">
            <img src="https://via.placeholder.com/300x200?text={name.replace(' ', '+')}" style="width: 250px; height: 180px;">
            <p>{name}</p>
        </div>
    """
gallery_html += '</div>'

create_page_q9("gallery.html", "Photo Gallery", gallery_html)

# 5. Contact
create_page_q9("contact.html", "Contact Information", """
    <p><strong>Tourism Office:</strong> Main City Square, Historic City.</p>
    <p><strong>Phone:</strong> 1800-123-TOUR</p>
    <p><strong>Email:</strong> visit@historiccity.com</p>
""")

# Generate 10 Site Pages
for i, (name, desc, era) in enumerate(sites):
    slug = f"site_{i+1}.html"
    create_page_q9(slug, name, f"""
        <img src="https://via.placeholder.com/800x400?text={name.replace(' ', '+')}" style="width:100%; border-radius: 8px; margin-bottom: 20px;">
        <h3>About {name}</h3>
        <p>{desc}</p>
        <h3>History</h3>
        <p>This site dates back to the {era}. It has witnessed centuries of history and stands as a testament to the architectural brilliance of that time.</p>
        <br>
        <a href="heritage.html" style="color: #8b4513; text-decoration: underline;">&larr; Back to Heritage Sites</a>
    """)

print("Successfully generated Q8 and Q9 websites.")
