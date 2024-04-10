<script>
    import Navbar from "./navbar.svelte";

    //Midlertidig JS løsning for min backend
    let kyoto
    function check_kyoto() {
        const kyoto_flag = "jj-ctf{hanafuda_kort}"

        if (kyoto_flag === kyoto){
            alert("Korrekt")
        }
        else{
            alert("Feil kode")
        }
    }

    let tokyo
    function check_tokyo() {
        const tokyo_flag = "jj-ctf{ramen_oppskrift}"

        if (tokyo_flag === tokyo){
            alert("Korrekt")
        }
        else{
            alert("Feil kode")
        }
    }

    let hiroshima
    function check_hiroshima() {
        const hiroshima_flag = "jj-ctf{mat_fra_hiroshima}"

        if(hiroshima_flag === hiroshima) {
            alert("Korrekt")
        }
        else{
            alert("Feil kode")
        }
    }
</script>

<div id="main">
    <Navbar/>
    <h1>Japan Julian-CTF</h1>
    <br>
    <img class="img" src="src/routes/images/kyoto-header-pciture.jpeg" alt="Pent Bildet :))">
    <br>
    <p id="story">Julian sitter fast i Japan, og trenger din hjelp til å finne hans tre eiendeler for å komme hjem. <br>
        Han husker bare at de ligger i tre byer, Kyoto, Tokyo og Hiroshima.
    </p>
    <form on:submit={check_kyoto}>
        <input type="text" id="kyoto" name="kyoto" placeholder="Kyoto eiendel" bind:value={kyoto}><br>
        <input type="submit" value="Submit">
    </form>
    <br>
    <form on:submit={check_tokyo}>
        <input type="text" id="tokyo" name="tokyo" placeholder="Tokyo eiendel" bind:value={tokyo}><br>
        <input type="submit" value="Submit">
    </form>
    <br>
    <form on:submit={check_hiroshima}>
        <input type="text" id="Hiroshima" name="Hiroshima" placeholder="Hiroshima eiendel" bind:value={hiroshima}><br>
        <input type="submit" value="Submit">
    </form>
</div>

<style>
    .img{
        width: 920px;
        height: 500px;
    }
</style>