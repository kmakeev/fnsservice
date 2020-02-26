function encode_utf8( s ) {
    return unescape( encodeURIComponent( JSON.stringify(s) ));
}

function decode_utf8( s ) {
    return JSON.parse(decodeURIComponent(escape(s[0])));
}