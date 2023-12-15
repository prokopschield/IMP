<script>
	export let display = false;
</script>

<div>
	<button on:click={() => (display = !display)}>
		{display ? 'Hide' : 'Show'} download links</button
	>

	{#if display}
		<ul>
			<li>
				<a
					target="_blank"
					href="https://v3cdn.nodesite.eu/NAZKPZ6iajEkulvvZNlEOmEMEXf4OTJAPar8i03QwRE/IMG_2265.MOV"
					download="IMG_2265.MOV"
				>
					Pokus #1 - IMG_2265.MOV
				</a>
			</li>
			<li>
				<a
					target="_blank"
					href="https://v3cdn.nodesite.eu/jW8u6ahPytpZgfTYVWM_SGT_6J2tEIczi34unh_jMa8/IMG_2265.mp4"
					download="IMG_2265.mp4"
				>
					Pokus #1 - IMG_2265.mp4
				</a>
			</li>
			<li>
				<a
					target="_blank"
					href="https://v3cdn.nodesite.eu/cc~aN_UlDVBxQTT0whPJCxKhWNmD2rm2GCCnBxlNjjk/IMG_2266.MOV"
					download="IMG_2266.MOV"
				>
					Pokus #2 - IMG_2266.MOV
				</a>
			</li>
			<li>
				<a
					target="_blank"
					href="https://v3cdn.nodesite.eu/VNSb0yc4rhU2oiHfHllebS0p3dnkVi0nqcvSNxc7fNk/IMG_2266.mp4"
					download="IMG_2266.mp4"
				>
					Pokus #2 - IMG_2266.mp4
				</a>
			</li>
			<li>
				<a
					target="_blank"
					href="https://v3cdn.nodesite.eu/Mk5KbAUI0l5GK1TNFOEqCCIeE6XmwjY6d3fBbN1W92U/IMG_2267.MOV"
					download="IMG_2267.MOV"
				>
					Pokus #3 - IMG_2267.MOV
				</a>
			</li>
			<li>
				<a
					target="_blank"
					href="https://v3cdn.nodesite.eu/ct5FUeM6SLiqMnNlW6Vv3WU9tPIumqWkLVa2EqCTGnM/IMG_2267.mp4"
					download="IMG_2267.mp4"
				>
					Pokus #3 - IMG_2267.mp4
				</a>
			</li>
		</ul>
	{/if}
</div>

<style>
	div {
		margin: 1em;
	}
	ul {
		list-style-type: none;
	}
</style>
