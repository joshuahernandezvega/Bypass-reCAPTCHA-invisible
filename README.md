# Bypass-reCAPTCHA-invisible
Have you ever wondered how you can get a valid recaptcha token to send a valid HTTP request? While doing web pentest for a client, I figured out this idea that can get you a token so that you can implement it with a Python function of your own to interact with your target. It might be not the best way, but it helped me a lot. 

IMPORTANT NOTE: This method works as long as the following options was disabled by the administrators:

![image](https://github.com/joshuahernandezvega/Bypass-reCAPTCHA-invisible/assets/31811373/b43ce646-3857-4ebb-ba50-97b2764dce2f)


Disclaimer: This has been made for ethical hacking purposes. Make sure you have the permissions if you´re using this against a target.

In order to use this script, we need to have the three files: get_token.py, process.php, and token.html in the same folder.

Then, if using a local server, we can start one using the following command:

php -S 0.0.0.0:8888

(You can modify the script if you want to use another port).

Now, we can just type python get_token.py. How it works is that:

1. A bot starts a new Firefox instance and visits localhost:8888/token.html.
2. Once the site has been loaded. it will immediately submit the invisible recaptcha (make sure you have placed your target key properly in token.html).
3. After the submission, we'll get a recaptcha response, and so the bot will auto-fill the fields for username and password and submit the form.
4. Once that's been submitted, the recaptcha token will travel along the username and password as a parameter in a get request that will be later processed by process.php.
5. Process.php will confirm that the Recaptcha token has been sent, and it will create a file called tokens.txt containing just one line with the most recent token.
6. The token will be read from the file and will be returned by the function.
7. Our personal function can send a request containing a valid Recaptcha token.

This is how the PHP server looks for the requests made by our bot:

![php server](https://github.com/joshuahernandezvega/Bypass-reCAPTCHA-invisible/assets/31811373/06a59ecf-7310-4a38-b7f6-a44ab3ef60ab)

This is how the script looks like with the sample function I added to get_token.py:

![get_token](https://github.com/joshuahernandezvega/Bypass-reCAPTCHA-invisible/assets/31811373/8680347f-651d-4953-b8d5-fe1c2c3174aa)




