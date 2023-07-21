let cards = []
let sum =0
let hasBlackJack = false
let isAlive = false
let message = ""
let messageEl = document.getElementById("message-el")
let sumel = document.getElementById("sum-el")
let cardel = document.getElementById("card-el")

let player ={
    Name : "subhash",
    Chips : 1000
}
let amount = document.getElementById("amount")
amount.textContent = player.Name +": $" + player.Chips


function startGame(){
    let fc = getRandomCard()
    let sc = getRandomCard()
    sum = fc + sc
    cards = [fc,sc]
    start_Game()
}

function start_Game(){

    cardel.textContent = "cards:"
    for (let i=0;i<cards.length;i++){
    cardel.textContent +=  cards[i] + " " 
    }
    sumel.textContent = "sum:" + sum
    if(sum <=20){
        message = "do you want to draw a new card"
        isAlive = true
    }
    else if(sum === 21){
        message = "wohooo!....blackjack"
        player.Chips += 100
        amount.textContent = player.Name +": $" + player.Chips
        hasBlackJack = true
        isAlive = false
    }
    else{
        message = "you are out of game"
        player.Chips -= 50
        amount.textContent = player.Name +": $" + player.Chips
        isAlive = false
    }
    messageEl.textContent = message
}

function newCard() {
    if(isAlive){
        let card = getRandomCard()
        sum += card
        cards.push(card)
        start_Game()
    }
}

function getRandomCard(){
    let card = Math.floor(Math.random()*13) + 1
    if (card > 10){
        return 10
    }
    else if(card === 1 ){
        return 11
    }
    else{
        return card
    }
}
    