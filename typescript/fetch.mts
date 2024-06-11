//fetch.mts

const API_URL = "https://api.github.com/search/repoositories?q=javascript"

const reponse = await fetch(API_URL)

if(!reponse.ok) {
    throw new Error("Request failed");
}

type QuicktypeTypes = {
    items : string[],
    image : string
}

const data = await reponse.json() as QuicktypeTypes

const repos = data.items.map(repo => {
    console.log(repo)
})