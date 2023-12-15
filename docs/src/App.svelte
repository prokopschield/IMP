<script lang="ts">
	import AutoEvalTable from "./AutoEvalTable.svelte";
	import DownloadLinks from "./DownloadLinks.svelte";

	let paused = true;
	let video: HTMLVideoElement;
	let version = 3;

	$: paused = Boolean(version);
</script>

<h1>Notepad--</h1>
<h3>projekt do předmětu IMP</h3>

<hr class="margin" />

<h2>Úvod do problematiky</h2>

<p>Zadání projektu je velice volné. Cílem projektu je</p>
<pre>
	"Na libovolném vývojovém kitu obsahujícím SoC ESP32 demonstrujte komunikaci
	jádra s periferním zařízením v podobě modulu s barevným TFT displejem
	připojeným přes SPI rozhraní. [...] Po inicializaci displeje bude možné skrze
	bezdrátové rozhraní WiFi/Bluetooth zaslat do vývojového kitu text či
	jednoduchou grafiku k zobrazení."
</pre>
<p>
	Přemýšlel jsem, co udělat kreativního, originálního, co by někoho pobavilo.
	<br />
	Pak mě napadlo udělat keylogger.
</p>

<h3>Plán</h3>

<p>
	Původní plán byl jednoduchý. Vytvořit webovou stránku, která by přes WS
	komunikovala <br /> stisky kláves serverové aplikaci, která by zároveň
	přijímala TCP spojení, kterým by stisky kláves předávala. <br /> Na tento server
	by se přes Wi-Fi připojil vývojový kit, který by přijaté znaky vykresloval na
	obrazovku.
</p>

<pre>
"Žádný plán nepřežije setkání s realitou."
	— Helmuth Karl Bernhard von Moltke
</pre>

<p>
	Při samotné implementaci jsem velice brzy narazil na to, že neumím pracovat
	s mikrokontrolery, <br /> a že bych se měl držet buď toho, co umím, nebo
	alespoň toho, co je standardní, <br /> protože na to už nejspíš existuje knihovna.
</p>

<h2>Zvolená architektura</h2>

<p>
	Na kitu běží v <a
		href="https://micropython.org/"
		target="_blank"
		rel="noopener noreferrer">MicroPythonu</a
	>
	webový server vytvořený
	<a
		href="https://randomnerdtutorials.com/micropython-wi-fi-manager-esp32-esp8266/"
		target="_blank"
		rel="noopener noreferrer">knihovnou</a
	>, kterou mi doporučil spolužák.
	<br />
	Ovládá TFT displej pomocí
	<a
		href="https://github.com/boochow/MicroPython-ST7735.git"
		target="_blank"
		rel="noopener noreferrer">knihovny pro práci s TFT displejem</a
	>.
</p>

<pre>
	"An idiot admires complexity, a genius admires simplicity"
				   — Terry A. Davis
</pre>

<h2>Popis aplikace</h2>

<p>
	Notepad-- je webová aplikace dostupná na místní síti, do které je kit
	připojen. <br /> Její vzhled (nefunkční kostru) lze vidět
	<a
		href="https://v3cdn.nodesite.eu/7GAHX_4iqEryFCm_MILpNSwF~Gpe5LYWG2_yKzLyvBo"
		target="_blank"
		rel="noopener noreferrer">zde</a
	>. <br /> Na stránce existuje keylogger, který kitu posílá informace o
	skisknutých klávesách pomocí
	<a
		href="https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API"
		target="_blank"
		rel="noopener noreferrer"><code>fetch</code></a
	>
	requestů. <br /> Kit poté vykresluje na TFT displeji všechna zmášknutá
	písmena, a
	<a
		href="https://datatracker.ietf.org/doc/html/rfc3986#section-2.3"
		target="_blank"
		rel="noopener noreferrer">některé další znaky</a
	>.
</p>

<h2>Demonstrační video</h2>
<p>
	Vznikly celkem tři pokusy nahrát video demonstrující aplikaci, <a
		href="https://v3cdn.nodesite.eu/ct5FUeM6SLiqMnNlW6Vv3WU9tPIumqWkLVa2EqCTGnM"
		target="_blank"
		rel="noopener noreferrer">třetí</a
	>
	se mi líbí nejvíc: <br />
	{#if version == 1}
		<!-- svelte-ignore a11y-media-has-caption -->
		<video
			controls
			bind:paused
			bind:this={video}
			style=" transform: rotate(270deg);"
		>
			<source
				src="https://v3cdn.nodesite.eu/NAZKPZ6iajEkulvvZNlEOmEMEXf4OTJAPar8i03QwRE.mov"
				type="video/quicktime"
			/>
			<source
				src="https://v3cdn.nodesite.eu/jW8u6ahPytpZgfTYVWM_SGT_6J2tEIczi34unh_jMa8.mp4"
				type="video/mp4"
			/>
		</video>
	{:else if version == 2}
		<!-- svelte-ignore a11y-media-has-caption -->
		<video controls playsinline bind:paused bind:this={video}>
			<source
				src="https://v3cdn.nodesite.eu/cc~aN_UlDVBxQTT0whPJCxKhWNmD2rm2GCCnBxlNjjk"
				type="video/quicktime"
			/>
			<source
				src="https://v3cdn.nodesite.eu/VNSb0yc4rhU2oiHfHllebS0p3dnkVi0nqcvSNxc7fNk"
				type="video/mp4"
			/>
		</video>
	{:else}
		<!-- svelte-ignore a11y-media-has-caption -->
		<video controls playsinline bind:paused bind:this={video}>
			<source
				src="https://v3cdn.nodesite.eu/Mk5KbAUI0l5GK1TNFOEqCCIeE6XmwjY6d3fBbN1W92U"
				type="video/quicktime"
			/>
			<source
				src="https://v3cdn.nodesite.eu/ct5FUeM6SLiqMnNlW6Vv3WU9tPIumqWkLVa2EqCTGnM"
				type="video/mp4"
			/>

			Video se nepodařilo načíst, klikněte na odkaz nad touto větou.
		</video>
	{/if}
	<br />
	<button
		on:click={() => {
			if (paused) {
				video.play();
			} else {
				video.pause();
			}
		}}
	>
		{#if paused}
			Play
		{:else}
			Pause
		{/if}
	</button>
	<br />
	<button on:click={() => (version = 1)}> Verze 1 </button>
	<button on:click={() => (version = 2)}> Verze 2 </button>
	<button on:click={() => (version = 3)}> Verze 3 </button>

	<DownloadLinks />
</p>

<hr class="margin" />

<h2>Autoevaluace</h2>

<p>
	Na to, že jsem projekt řešil až v posledních dvou týdnech před termínem
	odevzdání, si myslím, že dopadl velice hezky. <br /> Aplikace funguje tak, jak
	jsem si představoval, a kreativně plní zadání.
</p>

<p>
	Ačkoliv není snadné bez znalosti kontextu obecné praxe hodnocení v předmětu
	vlastní práci vyhodnocovat, <br /> vypracoval jsem následující odhad:
	<AutoEvalTable />
</p>

<hr />

<footer>
	Autor: Prokop Schield, student FIT VUT v Brně; prezentační technologie:
	<a href="https://svelte.dev" target="_blank" rel="noopener noreferrer"
		>Svelte</a
	>, šablona: default-dark
</footer>

<style>
	.margin {
		margin-top: 3em;
		margin-bottom: 5em;
	}

	button {
		margin-top: 0.3em;
	}

	footer {
		font-size: 1em;
	}
</style>
