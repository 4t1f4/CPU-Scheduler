<script lang="ts">
	import { resolve } from '$app/paths';

	type Category = {
		number: string;
		title: string;
		description: string;
		algorithms: readonly string[];
		count: string;
		href: '/cpu' | '/disk' | '/page-replacement' | '/deadlock';
		icon: string;
	};

	const stats = [
		{
			label: 'Total Algorithms',
			value: '14',
			description: 'Implemented in Python',
			icon: '⌘'
		},
		{
			label: 'Algorithm Categories',
			value: '04',
			description: 'Core OS concepts',
			icon: '▦'
		},
		{
			label: 'API Endpoints',
			value: '14',
			description: 'Available in FastAPI',
			icon: '⌁'
		},
		{
			label: 'Simulations Run',
			value: '00',
			description: 'Start your first simulation',
			icon: '▷'
		}
	];

	const categories: Category[] = [
		{
			number: '01',
			title: 'CPU Scheduling',
			description: 'Explore how the operating system allocates CPU time to competing processes.',
			algorithms: ['FCFS', 'SJF', 'SRTF', 'Priority', 'Round Robin'],
			count: '05 Algorithms',
			href: '/cpu',
			icon: '◫'
		},
		{
			number: '02',
			title: 'Disk Scheduling',
			description: 'Visualize disk head movement and understand how requests are serviced.',
			algorithms: ['FCFS', 'SSTF', 'SCAN', 'C-SCAN'],
			count: '04 Algorithms',
			href: '/disk',
			icon: '◉'
		},
		{
			number: '03',
			title: 'Page Replacement',
			description: 'Understand how memory frames are managed when a page fault occurs.',
			algorithms: ['FIFO', 'Optimal', 'LRU'],
			count: '03 Algorithms',
			href: '/page-replacement',
			icon: '▦'
		},
		{
			number: '04',
			title: 'Deadlock Management',
			description: 'Study resource allocation, safe sequences and deadlock detection.',
			algorithms: ['Banker’s Algorithm', 'Deadlock Detection'],
			count: '02 Algorithms',
			href: '/deadlock',
			icon: '⇄'
		}
	];

	const workflow = [
		{
			step: '01',
			title: 'Choose an algorithm',
			detail: 'Select an algorithm from any category.'
		},
		{
			step: '02',
			title: 'Configure your inputs',
			detail: 'Enter processes, requests, frames or resources.'
		},
		{
			step: '03',
			title: 'Run the simulation',
			detail: 'Execute the algorithm through the backend.'
		},
		{
			step: '04',
			title: 'Analyze the results',
			detail: 'Understand the execution through visualizations.'
		}
	] as const;

	const systemInfo = [
		{ label: 'Frontend', value: 'SvelteKit + TypeScript' },
		{ label: 'Styling', value: 'TailwindCSS' },
		{ label: 'Backend', value: 'Python + FastAPI' },
		{ label: 'Algorithm Engine', value: 'Python' }
	];
</script>

<svelte:head>
	<title>Dashboard | OS Simulator</title>
</svelte:head>

<div class="space-y-10">
	<!-- Welcome section -->
	<section
		class="relative overflow-hidden rounded-2xl border border-cyan-400/10 bg-gradient-to-br from-[#111E31] via-[#101827] to-[#0D1320] p-7 sm:p-10"
	>
		<div
			class="pointer-events-none absolute -top-32 -right-20 h-80 w-80 rounded-full bg-cyan-400/[0.07] blur-3xl"
		></div>

		<div class="relative z-10 max-w-2xl">
			<div
				class="mb-5 inline-flex items-center gap-2 rounded-full border border-cyan-400/20 bg-cyan-400/[0.07] px-3 py-1.5"
			>
				<span class="h-1.5 w-1.5 rounded-full bg-cyan-400"></span>
				<span class="text-[10px] font-semibold tracking-[0.15em] text-cyan-300">
					OPERATING SYSTEMS LAB
				</span>
			</div>

			<h1 class="text-3xl leading-tight font-bold tracking-tight text-white sm:text-4xl">
				Understand the logic.
				<span class="text-cyan-400"> Visualize the execution. </span>
			</h1>

			<p class="mt-4 max-w-xl text-sm leading-7 text-slate-400 sm:text-base">
				An interactive environment to explore Operating System algorithms, experiment with different
				inputs and understand how they work behind the scenes.
			</p>

			<a
				href={resolve('/cpu')}
				class="mt-7 inline-flex items-center gap-3 rounded-lg bg-cyan-400 px-5 py-3 text-sm font-semibold text-[#07111B] transition hover:bg-cyan-300"
			>
				Explore algorithms
				<span>→</span>
			</a>
		</div>

		<div
			class="pointer-events-none absolute right-8 bottom-5 hidden text-8xl font-black text-white/[0.025] select-none lg:block"
		>
			OS
		</div>
	</section>

	<!-- Statistics -->
	<section>
		<div class="mb-5 flex items-center justify-between">
			<div>
				<h2 class="text-lg font-semibold text-white">Project Overview</h2>
				<p class="mt-1 text-xs text-slate-500">A quick look at your algorithm engine.</p>
			</div>
		</div>

		<div class="grid grid-cols-1 gap-4 sm:grid-cols-2 xl:grid-cols-4">
			{#each stats as stat (stat.label)}
				<div
					class="rounded-xl border border-white/[0.07] bg-[#0D1320] p-5 transition hover:border-cyan-400/20"
				>
					<div class="flex items-center justify-between">
						<p class="text-xs font-medium text-slate-400">
							{stat.label}
						</p>

						<span
							class="flex h-9 w-9 items-center justify-center rounded-lg bg-cyan-400/[0.08] text-lg text-cyan-400"
						>
							{stat.icon}
						</span>
					</div>

					<h3 class="mt-5 text-3xl font-bold tracking-tight text-white">
						{stat.value}
					</h3>

					<p class="mt-2 text-[11px] text-slate-500">
						{stat.description}
					</p>
				</div>
			{/each}
		</div>
	</section>

	<!-- Algorithm categories -->
	<section>
		<div class="mb-5 flex flex-wrap items-end justify-between gap-3">
			<div>
				<h2 class="text-lg font-semibold text-white">Algorithm Workspaces</h2>
				<p class="mt-1 text-xs text-slate-500">Choose a category to start experimenting.</p>
			</div>

			<span class="text-xs text-slate-500"> 4 Categories available </span>
		</div>

		<div class="grid grid-cols-1 gap-5 lg:grid-cols-2">
			{#each categories as category (category.number)}
				<a
					href={resolve(category.href)}
					class="group rounded-xl border border-white/[0.07] bg-[#0D1320] p-6 transition duration-300 hover:-translate-y-1 hover:border-cyan-400/30 hover:bg-[#111B2B]"
				>
					<div class="flex items-start justify-between">
						<div class="flex items-center gap-4">
							<div
								class="flex h-12 w-12 items-center justify-center rounded-xl border border-cyan-400/10 bg-cyan-400/[0.07] text-2xl text-cyan-400"
							>
								{category.icon}
							</div>

							<div>
								<p class="text-[10px] font-semibold tracking-widest text-cyan-500">
									{category.number} / WORKSPACE
								</p>

								<h3
									class="mt-1 text-base font-semibold text-white transition group-hover:text-cyan-300"
								>
									{category.title}
								</h3>
							</div>
						</div>

						<span
							class="text-xl text-slate-600 transition group-hover:translate-x-1 group-hover:text-cyan-400"
						>
							→
						</span>
					</div>

					<p class="mt-5 min-h-12 text-sm leading-6 text-slate-400">
						{category.description}
					</p>

					<div class="mt-5 flex flex-wrap gap-2">
						{#each category.algorithms as algorithm (algorithm)}
							<span
								class="rounded-md border border-white/[0.07] bg-white/[0.03] px-2.5 py-1.5 text-[10px] font-medium text-slate-400"
							>
								{algorithm}
							</span>
						{/each}
					</div>

					<div class="mt-6 flex items-center justify-between border-t border-white/[0.07] pt-4">
						<span class="text-[11px] text-slate-500">
							{category.count}
						</span>

						<span class="text-xs font-medium text-cyan-400"> Open workspace → </span>
					</div>
				</a>
			{/each}
		</div>
	</section>

	<!-- Bottom information -->
	<section class="grid grid-cols-1 gap-5 lg:grid-cols-2">
		<!-- Workflow -->
		<div class="rounded-xl border border-white/[0.07] bg-[#0D1320] p-6">
			<h3 class="text-sm font-semibold text-white">How it works</h3>

			<div class="mt-5 space-y-4">
				{#each workflow as item (item.step)}
					<div class="flex items-start gap-4">
						<span class="text-xs font-bold text-cyan-400">
							{item.step}
						</span>

						<div>
							<p class="text-xs font-medium text-slate-200">
								{item.title}
							</p>
							<p class="mt-1 text-[11px] text-slate-500">
								{item.detail}
							</p>
						</div>
					</div>
				{/each}
			</div>
		</div>

		<!-- System information -->
		<div class="rounded-xl border border-white/[0.07] bg-[#0D1320] p-6">
			<div class="flex items-center justify-between">
				<h3 class="text-sm font-semibold text-white">System Information</h3>

				<span class="rounded-md bg-white/[0.04] px-2 py-1 text-[10px] text-slate-500">
					DEVELOPMENT
				</span>
			</div>

			<div class="mt-5 space-y-4">
				{#each systemInfo as info (info.label)}
					<div
						class="flex flex-wrap items-center justify-between gap-2 border-b border-white/[0.05] pb-3"
					>
						<span class="text-xs text-slate-500">
							{info.label}
						</span>

						<span class="text-xs font-medium text-slate-300">
							{info.value}
						</span>
					</div>
				{/each}
			</div>
		</div>
	</section>
</div>
