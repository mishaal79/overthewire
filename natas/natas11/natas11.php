<?php



function xor_encrypt($in) {
    $key = 'qw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jq';
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

echo base64_encode((xor_encrypt(json_encode(array("showpassword"=>"yes", "bgcolor"=>"#ffffff")))));
echo json_encode(array("showpassword"=>"yes", "bgcolor"=>"#ffffff"));
?>