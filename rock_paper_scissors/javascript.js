let result = document.getElementById("result")
let playerScore = document.getElementById("playerscore")
let hands = document.getElementById("hands")
let endgameButton = document.getElementById('endgamebutton')

let totalScore = { 'humanScore':0 }

function computerChoice(){
    const arr = ["rock",'paper','scissors']
    return arr[Math.floor((Math.random()*3))]
}

endgameButton.onclick=(totalScore)=>{
    endGame(totalScore)
}

function getResult(humanChoice,computerChoice){

    let score = 0
    if (computerChoice == humanChoice){
        score=0
    }
    else if(humanChoice == "rock" && computerChoice =="scissors" || humanChoice == "paper" && computerChoice == "rock" || humanChoice == "scissors" && computerChoice == "paper"){
        score=1
    }
    else{
        score=-1
    }
    return score

}

function playgame(){
    let userChoices = document.querySelectorAll(".button")
    userChoices.forEach(userChoice=>{
        userChoice.onclick=()=>{
            humanChoice(userChoice.value)
        }
    })
     
}

function humanChoice(humanChoose){
    const computerChoose = computerChoice()
    const result=getResult(humanChoose,computerChoose)
    totalScore['humanScore']+=result
    showResult(result,humanChoose,computerChoose)

}
function showResult(score,humanChoose,computerChoose){
    if (score==1){
        result.innerText="you Won!"
    }else if (score == -1){
        result.innerText="you Lose!"
    }
    else{
        result.innerText="it's a tie!"
    }
    playerScore.innerText=totalScore['humanScore']
    hands.innerText=`🧑${humanChoose} Vs 🤖${computerChoose}`

}
function endGame(totalScore){
    totalScore['humanScore'] = 0
    result.innerText=''
    hands.innerText=''
    playerScore.innerText=''

}
playgame()

