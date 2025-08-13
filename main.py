#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util


class MainHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write("""
       <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Age Calculator</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', sans-serif;
            background: linear-gradient(to right, #74ebd5, #ACB6E5);
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .container {
            background-color: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 0 10px rgba(0,0,0,0.2);
            text-align: center;
            width: 300px;
        }
        input {
            width: 80%;
            padding: 10px;
            margin: 8px 0;
            font-size: 16px;
            border: 1px solid #ccc;
            border-radius: 6px;
        }
        button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            font-size: 16px;
            border-radius: 6px;
            cursor: pointer;
        }
        h2 {
            margin-bottom: 20px;
        }
        #result {
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>🧮 Age Calculator</h2>
        <input type="number" id="year" placeholder="Year (YYYY)" required><br>
        <input type="number" id="month" placeholder="Month (MM)" required><br>
        <input type="number" id="day" placeholder="Day (DD)" required><br>
        <button onclick="calculateAge()">Calculate Age</button>
        <div id="result"></div>
    </div>

    <script>
        function calculateAge() {
            const year = parseInt(document.getElementById('year').value);
            const month = parseInt(document.getElementById('month').value);
            const day = parseInt(document.getElementById('day').value);

            if (!year || !month || !day) {
                document.getElementById('result').innerHTML = "<p style='color:red;'>Please enter a valid date.</p>";
                return;
            }

            const birthDate = new Date(year, month - 1, day);
            const today = new Date();
            const ageInMs = today - birthDate;

            if (ageInMs < 0) {
                document.getElementById('result').innerHTML = "<p style='color:red;'>Birthdate is in the future!</p>";
                return;
            }

            const ageDate = new Date(ageInMs);
            const years = today.getFullYear() - birthDate.getFullYear();
            const months = (today.getFullYear() - birthDate.getFullYear()) * 12 + today.getMonth() - birthDate.getMonth();
            const days = Math.floor(ageInMs / (1000 * 60 * 60 * 24));

            // Next birthday countdown
            let nextBirthday = new Date(today.getFullYear(), birthDate.getMonth(), birthDate.getDate());
            if (nextBirthday < today) {
                nextBirthday.setFullYear(today.getFullYear() + 1);
            }
            const countdownDays = Math.ceil((nextBirthday - today) / (1000 * 60 * 60 * 24));

            document.getElementById('result').innerHTML = `
                <h3>🎉 You are ${years} years, ${months} months, and ${days} days old.</h3>
                <h4>⏳ ${countdownDays} days until your next birthday!</h4>
            `;
        }
    </script>
</body>
</html>
""")


def main():
    application = webapp.WSGIApplication([('/', MainHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
