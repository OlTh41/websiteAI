<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Retrieve and sanitize form data
    $firstname = htmlspecialchars($_POST['firstname']);
    $lastname = htmlspecialchars($_POST['lastname']);
    $subject = htmlspecialchars($_POST['subject']);

    // Save the data to a file
    $file = fopen("submissions.txt", "a");
    fwrite($file, "Firstname: " . $firstname . "\n");
    fwrite($file, "Lastname: " . $lastname . "\n");
    fwrite($file, "Subject: " . $subject . "\n\n");
    fclose($file);

    // Provide a response
    echo "Thank you, $firstname $lastname. Your message has been received.";
}
?>
