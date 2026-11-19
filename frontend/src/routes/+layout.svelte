<script lang="ts">
	import './layout.css';
	import favicon from '#lib/assets/favicon.svg';
	import type { LayoutProps } from './$types';
	import { page } from '$app/state';
	import { resolve } from '$app/paths';

	let { children }: LayoutProps = $props();

	let mobileNavOpen = $state(false);

	const navItems = [
		{ label: 'Dashboard', href: '/', icon: '⌂' },
		{ label: 'CPU Scheduling', href: '/cpu', icon: '◫' },
		{ label: 'Disk Scheduling', href: '/disk', icon: '◉' },
		{ label: 'Page Replacement', href: '/page-replacement', icon: '▦' },
		{ label: 'Deadlock', href: '/deadlock', icon: '⇄' }
	] as const;
</script>

<svelte:head>
	<title>OS Simulator | Algorithm Visualizer</title>
	<meta name="description" content="Interactive Operating System Algorithm Simulator" />
	<link rel="icon" href={favicon} />
</svelte:head>

<div class="min-h-screen bg-[#090D16] text-slate-200">
	<!-- Mobile overlay -->
	{#if mobileNavOpen}
		<button
			class="fixed inset-0 z-40 bg-black/60 lg:hidden"
			aria-label="Close navigation"
			onclick={() => (mobileNavOpen = false)}
		></button>
	{/if}

	<div class="flex min-h-screen">
		<!-- Sidebar -->
		<aside
			class={`fixed inset-y-0 left-0 z-50 flex w-64 flex-col border-r border-white/[0.07] bg-[#0D1320] transition-transform duration-300 lg:sticky lg:top-0 lg:h-screen lg:translate-x-0 ${
				mobileNavOpen ? 'translate-x-0' : '-translate-x-full'
			}`}
		>
			<!-- Logo -->
			<div class="flex h-20 items-center gap-3 border-b border-white/[0.07] px-6">
				<div
					class="flex h-10 w-10 items-center justify-center rounded-xl bg-cyan-400/10 text-xl text-cyan-400"
				>
					⌘
				</div>

				<div>
					<h1 class="text-sm font-bold tracking-wide text-white">OS SIMULATOR</h1>
					<p class="text-[11px] tracking-wider text-slate-500">ALGORITHM VISUALIZER</p>
				</div>
			</div>

			<!-- Navigation -->
			<div class="flex-1 px-4 py-7">
				<p class="mb-4 px-3 text-[10px] font-semibold tracking-[0.2em] text-slate-500">WORKSPACE</p>

				<nav class="space-y-1">
					{#each navItems as item (item.href)}
						<a
							href={resolve(item.href)}
							aria-current={page.url.pathname === resolve(item.href) ? 'page' : undefined}
							onclick={() => (mobileNavOpen = false)}
							class={`flex items-center gap-3 rounded-lg px-3 py-3 text-sm transition-all ${
								page.url.pathname === resolve(item.href)
									? 'border border-cyan-400/10 bg-cyan-400/10 font-medium text-cyan-400'
									: 'text-slate-400 hover:bg-white/[0.04] hover:text-white'
							}`}
						>
							<span class="w-5 text-center text-lg">
								{item.icon}
							</span>

							{item.label}

							{#if page.url.pathname === resolve(item.href)}
								<span class="ml-auto h-1.5 w-1.5 rounded-full bg-cyan-400"></span>
							{/if}
						</a>
					{/each}
				</nav>

				<!-- Project information -->
				<div class="mt-10 border-t border-white/[0.07] pt-6">
					<p class="mb-4 px-3 text-[10px] font-semibold tracking-[0.2em] text-slate-500">PROJECT</p>

					<div class="rounded-xl border border-white/[0.07] bg-white/[0.02] p-4">
						<div class="mb-2 flex items-center gap-2">
							<span class="h-2 w-2 rounded-full bg-emerald-400"></span>
							<span class="text-xs font-medium text-slate-300"> Backend project </span>
						</div>

						<p class="text-[11px] leading-relaxed text-slate-500">
							FastAPI · Python · Algorithm Engine
						</p>
					</div>
				</div>
			</div>

			<!-- Sidebar footer -->
			<div class="border-t border-white/[0.07] p-5">
				<p class="text-xs text-slate-500">Built for learning OS concepts.</p>
				<p class="mt-1 text-[10px] text-slate-600">OS Algorithm Simulator · v1.0</p>
			</div>
		</aside>

		<!-- Main application -->
		<div class="min-w-0 flex-1">
			<!-- Topbar -->
			<header
				class="sticky top-0 z-30 flex h-20 items-center justify-between border-b border-white/[0.07] bg-[#090D16]/90 px-5 backdrop-blur-xl sm:px-8"
			>
				<div class="flex items-center gap-4">
					<button
						class="rounded-lg border border-white/10 p-2 text-slate-400 hover:bg-white/5 lg:hidden"
						aria-label="Open navigation"
						onclick={() => (mobileNavOpen = true)}
					>
						☰
					</button>

					<div>
						<p class="text-xs text-slate-500">OS Algorithm Simulator</p>
						<p class="mt-1 text-sm font-semibold text-white">
							{navItems.find((item) => resolve(item.href) === page.url.pathname)?.label ??
								'Workspace'}
						</p>
					</div>
				</div>

				<div class="flex items-center gap-3">
					<div
						class="hidden items-center gap-2 rounded-full border border-amber-400/10 bg-amber-400/[0.05] px-3 py-2 sm:flex"
					>
						<span class="h-1.5 w-1.5 rounded-full bg-amber-400"></span>
						<span class="text-[11px] text-amber-300"> API not connected </span>
					</div>

					<div
						class="flex h-9 w-9 items-center justify-center rounded-full border border-cyan-400/20 bg-cyan-400/10 text-xs font-bold text-cyan-400"
					>
						OS
					</div>
				</div>
			</header>

			<!-- Current route -->
			<main class="mx-auto w-full max-w-[1600px] p-5 sm:p-8 lg:p-10">
				{@render children()}
			</main>
		</div>
	</div>
</div>
