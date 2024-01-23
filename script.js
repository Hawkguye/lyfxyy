let audios = document.getElementsByTagName("audio");

let audioRate = 1;

function updateText(){
    document.getElementById("audioSpeed").innerText = "语音速度:  " + audioRate.toFixed(1) + " 倍"
}

function changeSpeed(rate) {
    audioRate += rate;
    for (let i = 0; i < audios.length; i++){
        audios[i].playbackRate += rate;
    }
    updateText();
}

function natralizeSpeed() {
    audioRate = 1;
    for (let i = 0; i < audios.length; i++){
        audios[i].playbackRate = 1;
    }
    updateText();
}