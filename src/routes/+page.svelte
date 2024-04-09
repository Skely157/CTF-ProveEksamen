<script>
    import Navbar from "./navbar.svelte";

    function check_kyoto() {
        const kyoto_flag = "jj-ctf{hanafuda_kort}"

        if (kyoto_flag === kyoto){
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

    <img class="img" src="/Users/juela002/Documents/GitHub/CTF-ProveEksamen/src/routes/images/kyoto-header-pciture.jpeg" alt="Pent Bildet :))">
    <br>

    <p id="story">Julian sitter fast i Japan, og trenger din hjelp til å finne hans tre eiendeler for å komme hjem. <br>
        Han husker bare at de ligger i tre byer, Kyoto, Tokyo og Hiroshima.
    </p>

    <form onsubmit=check_kyoto()>
        <input type="text" id="kyoto" name="kyoto" placeholder="Kyoto eiendel"><br>
        <input type="submit" value="Submit">
    </form>
    <br>
    <form>
        <input type="text" id="tokyo" name="tokyo" placeholder="Tokyo eiendel"><br>
        <input type="submit" value="Submit">
    </form>
    <br>
    <form>
        <input type="text" id="Hiroshima" name="Hiroshima" placeholder="Hiroshima eiendel"><br>
        <input type="submit" value="Submit">
    </form>
</div>

<style>
    .img{
        width: 100px;
        height: 100px;
    }
</style>