function toggleSidebar() {
    const sidebar = document.getElementById('menuSidebar');
    const overlay = document.getElementById('menuOverlay');

    if (!sidebar || !overlay) {
        console.warn("❗ Elementos del menú no encontrados.");
        return;
    }

    const isOpen = sidebar.classList.contains('open');
    sidebar.classList.toggle('open');
    overlay.classList.toggle('active');
    document.body.style.overflow = isOpen ? '' : 'hidden';
}
