<?php
    $default = '<?xml version=\'1.0\' encoding="ISO-8859-1"?>
<users>
    <user>
        <name>Jean</name>
        <email>jean@test.com</email>
    </user>

    <user>
        <name>Pierre</name>
        <email>pierre@test.com</email>
    </user>

    <user>
        <name>Paul</name>
        <email>paul@test.com</email>
    </user>
    
    <user>
        <name>Jacque</name>
        <email>jacque@test.com</email>
  </user>
</users>';
//flag in flag.txt
    $result = "";
    if(isset($_POST['content']))
    {
        $dom = new DOMDocument();
        $dom->loadXML($_POST['content'],LIBXML_NOENT);
        
        $xmlstr = $dom->saveXML();
        $xml= new SimpleXMLElement($xmlstr);
        
        foreach($xml as $users)
        {
            $result .= "<div>".$users->name." email address is ".$users->email."</div>";
        }
    }
    $content = '
	<div id="container">
		<div>
		    <h1>Directory</h1>
                    <div>
                        <form action="" id="form" autocomplete="off" method="POST">
                            <textarea form ="form" name="content" rows="30" cols="100" wrap="soft">'.$default.'</textarea></br>
                            <button type="submit">Test it</button>
                        </form>
                        <div>
                        '.$result.'
                        </div>
                    </div>
		</div>
	</div>';
    
    
?>
<!DOCTYPE html>
<html><head>
    <meta http-equiv="content-type" content="text/html; charset=UTF-8">
    <title>Directory</title>
    <meta charset="utf-8">
</head>

<body>
<?php echo $content;?>
</body>
</html> 
