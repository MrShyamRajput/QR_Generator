import qrcode
upi_id="7378869398-4@ybl"
phonepe_url=f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
paytm_url=f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
google_pay_url=f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"

#create Qr code for each payment app
qr=qrcode.make(phonepe_url)
paytm_qr=qrcode.make(paytm_url)
google_qr=qrcode.make(google_pay_url)

#Display the QR codes
qr.show()


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Display QR Code</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: linear-gradient(120deg, #89f7fe, #66a6ff);
            color: #333;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
            overflow: hidden;
        }

        .container {
            text-align: center;
            background: #fff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .container:hover {
            transform: translateY(-10px);
            box-shadow: 0 15px 40px rgba(0, 0, 0, 0.2);
        }

        h1 {
            font-size: 2rem;
            margin-bottom: 10px;
            color: #333;
            animation: fadeIn 1s ease-in-out;
        }

        .qr-container {
            position: relative;
            display: inline-block;
            margin: 20px 0;
        }

        .qr-container img {
            width: 200px;
            height: 200px;
            border: 5px solid #66a6ff;
            border-radius: 10px;
            animation: zoomIn 0.8s ease-in-out;
        }

        .btn {
            display: inline-block;
            padding: 10px 20px;
            background: #66a6ff;
            color: #fff;
            text-decoration: none;
            border-radius: 5px;
            font-size: 1rem;
            transition: background 0.3s ease, transform 0.3s ease;
        }

        .btn:hover {
            background: #89f7fe;
            transform: scale(1.1);
        }

        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes zoomIn {
            from {
                transform: scale(0.5);
                opacity: 0;
            }
            to {
                transform: scale(1);
                opacity: 1;
            }
        }
    </style>
</head>
<body>
    {% load static %}
    <div class="container">
        <h1>Your QR Code</h1>
        <div class="qr-container">
            <!-- Replace 'qr_code.png' with the actual file name of the saved QR code -->
            <img src="{% static 'images/7378869398-4@ybl.png' %}" alt="{{file_path}}">
        </div>
        <a href="images/7378869398-4@ybl.png" class="btn" download>Download QR Code</a>
    </div>
</body>
</html>
