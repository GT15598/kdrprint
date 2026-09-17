document.addEventListener('DOMContentLoaded', function () {
	const mobileMenu = document.querySelector('.mobile-menu');
	const mobileNav = document.querySelector('.mobile-nav');

	if (!mobileMenu || !mobileNav) {
		return;
	}

	function closeMenu() {
		mobileMenu.classList.remove('active');
		mobileNav.classList.remove('active');
		document.body.classList.remove('menu-open');
		mobileMenu.setAttribute('aria-expanded', 'false');
		mobileMenu.setAttribute('aria-label', 'Мәзірді ашу');
	}

	mobileMenu.addEventListener('click', function () {
		const isOpen = !mobileNav.classList.contains('active');

		if (isOpen) {
			mobileMenu.classList.add('active');
			mobileNav.classList.add('active');
			document.body.classList.add('menu-open');
			mobileMenu.setAttribute('aria-expanded', 'true');
			mobileMenu.setAttribute('aria-label', 'Мәзірді жабу');
		} else {
			closeMenu();
		}
	});

	mobileNav.querySelectorAll('a').forEach(function (link) {
		link.addEventListener('click', closeMenu);
	});

	document.addEventListener('keydown', function (event) {
		if (event.key === 'Escape') {
			closeMenu();
		}
	});
});
