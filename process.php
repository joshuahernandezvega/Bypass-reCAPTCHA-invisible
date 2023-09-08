<?php
$recaptchaToken = isset($_GET['g-recaptcha-response']) ? $_GET['g-recaptcha-response'] : '';

if (!empty($recaptchaToken)) {
    //we write the token into a file
    $file = fopen('tokens.txt', 'a');
    fwrite($file, $recaptchaToken . "\n");
    fclose($file);
}
?>
