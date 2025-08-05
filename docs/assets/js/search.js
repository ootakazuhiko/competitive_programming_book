/**
 * Search Functionality
 * Provides real-time search across book content with highlighting and keyboard navigation
 */

class SearchManager {
    constructor() {
        this.searchInput = null;
        this.searchResults = null;
        this.searchData = [];
        this.isLoading = false;
        this.currentResultIndex = -1;
        this.searchTimeout = null;
        
        this.init();
    }

    async init() {
        this.searchInput = document.getElementById('search-input');
        this.searchResults = document.getElementById('search-results');
        
        if (!this.searchInput || !this.searchResults) {
            return;
        }

        await this.loadSearchData();
        this.setupEventListeners();
    }

    async loadSearchData() {
        if (this.isLoading) return;
        
        this.isLoading = true;
        
        try {
            // Get base URL for the site
            const baseUrl = window.location.origin + window.location.pathname.replace(/[^/]*$/, '');
            
            // Try to load search data from a JSON file (if available)
            try {
                const response = await fetch(`${baseUrl}search-data.json`);
                if (response.ok) {
                    this.searchData = await response.json();
                    return;
                }
            } catch (e) {
                // Fall back to extracting from current page content
            }
            
            // Fallback: Create search data from navigation
            this.createSearchDataFromNavigation();
            
        } catch (error) {
            console.warn('Failed to load search data:', error);
            this.createSearchDataFromNavigation();
        } finally {
            this.isLoading = false;
        }
    }

    createSearchDataFromNavigation() {
        // Extract searchable content from sidebar navigation
        const navLinks = document.querySelectorAll('.toc-link, .toc-sublink');
        const searchData = [];
        
        navLinks.forEach(link => {
            const title = link.textContent.trim();
            const url = link.getAttribute('href');
            
            if (title && url) {
                searchData.push({
                    title: title,
                    url: url,
                    content: title, // Use title as content for basic search
                    type: link.classList.contains('toc-sublink') ? 'subsection' : 'chapter'
                });
            }
        });
        
        this.searchData = searchData;
    }

    setupEventListeners() {
        // Search input
        this.searchInput.addEventListener('input', (e) => {
            const query = e.target.value.trim();
            this.handleSearchInput(query);
        });

        // Keyboard navigation
        this.searchInput.addEventListener('keydown', (e) => {
            this.handleKeyboardNavigation(e);
        });

        // Focus management
        this.searchInput.addEventListener('focus', () => {
            if (this.searchInput.value.trim()) {
                this.showResults();
            }
        });

        // Click outside to close
        document.addEventListener('click', (e) => {
            if (!e.target.closest('.search-container')) {
                this.hideResults();
            }
        });

        // Escape key to close
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                this.hideResults();
                this.searchInput.blur();
            }
        });
    }

    handleSearchInput(query) {
        // Clear previous timeout
        if (this.searchTimeout) {
            clearTimeout(this.searchTimeout);
        }

        // Debounce search
        this.searchTimeout = setTimeout(() => {
            this.performSearch(query);
        }, 150);
    }

    performSearch(query) {
        if (!query || query.length < 2) {
            this.hideResults();
            return;
        }

        const results = this.searchInData(query);
        this.displayResults(results, query);
    }

    searchInData(query) {
        const lowerQuery = query.toLowerCase();
        const results = [];

        this.searchData.forEach(item => {
            const titleMatch = item.title.toLowerCase().includes(lowerQuery);
            const contentMatch = item.content && item.content.toLowerCase().includes(lowerQuery);
            
            if (titleMatch || contentMatch) {
                // Calculate relevance score
                let score = 0;
                if (item.title.toLowerCase().startsWith(lowerQuery)) {
                    score += 10; // Exact start match gets highest score
                } else if (titleMatch) {
                    score += 5; // Title match gets medium score
                }
                if (contentMatch) {
                    score += 2; // Content match gets lower score
                }

                results.push({
                    ...item,
                    score: score,
                    highlightedTitle: this.highlightText(item.title, query),
                    highlightedContent: item.content ? this.highlightText(item.content.substring(0, 150), query) : null
                });
            }
        });

        // Sort by relevance score and then alphabetically
        return results.sort((a, b) => {
            if (b.score !== a.score) {
                return b.score - a.score;
            }
            return a.title.localeCompare(b.title);
        }).slice(0, 8); // Limit to 8 results
    }

    highlightText(text, query) {
        if (!text || !query) return text;
        
        const regex = new RegExp(`(${this.escapeRegex(query)})`, 'gi');
        return text.replace(regex, '<mark>$1</mark>');
    }

    escapeRegex(string) {
        return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    }

    displayResults(results, query) {
        if (!results.length) {
            this.searchResults.innerHTML = `
                <div class="search-no-results">
                    「${this.escapeHtml(query)}」の検索結果はありません
                </div>
            `;
            this.showResults();
            return;
        }

        const resultHtml = results.map((result, index) => `
            <a href="${result.url}" 
               class="search-result-item" 
               data-index="${index}"
               onclick="this.closest('.search-container').querySelector('.search-input').blur()">
                <div class="search-result-title">${result.highlightedTitle}</div>
                ${result.highlightedContent && result.highlightedContent !== result.highlightedTitle ? 
                    `<div class="search-result-content">${result.highlightedContent}...</div>` : ''}
                <div class="search-result-type">${result.type === 'chapter' ? '章' : '節'}</div>
            </a>
        `).join('');

        this.searchResults.innerHTML = resultHtml;
        this.currentResultIndex = -1;
        this.showResults();
    }

    showResults() {
        this.searchResults.style.display = 'block';
    }

    hideResults() {
        this.searchResults.style.display = 'none';
        this.currentResultIndex = -1;
        this.clearHighlight();
    }

    handleKeyboardNavigation(e) {
        const resultItems = this.searchResults.querySelectorAll('.search-result-item');
        
        if (!resultItems.length) return;

        switch (e.key) {
            case 'ArrowDown':
                e.preventDefault();
                this.currentResultIndex = Math.min(this.currentResultIndex + 1, resultItems.length - 1);
                this.highlightResult();
                break;
                
            case 'ArrowUp':
                e.preventDefault();
                this.currentResultIndex = Math.max(this.currentResultIndex - 1, -1);
                this.highlightResult();
                break;
                
            case 'Enter':
                e.preventDefault();
                if (this.currentResultIndex >= 0 && resultItems[this.currentResultIndex]) {
                    resultItems[this.currentResultIndex].click();
                }
                break;
        }
    }

    highlightResult() {
        const resultItems = this.searchResults.querySelectorAll('.search-result-item');
        
        // Clear previous highlights
        this.clearHighlight();
        
        // Highlight current result
        if (this.currentResultIndex >= 0 && resultItems[this.currentResultIndex]) {
            resultItems[this.currentResultIndex].classList.add('search-highlighted');
            resultItems[this.currentResultIndex].scrollIntoView({
                block: 'nearest',
                behavior: 'smooth'
            });
        }
    }

    clearHighlight() {
        const highlighted = this.searchResults.querySelectorAll('.search-highlighted');
        highlighted.forEach(item => item.classList.remove('search-highlighted'));
    }

    escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    // Public API
    clear() {
        this.searchInput.value = '';
        this.hideResults();
    }

    focus() {
        this.searchInput.focus();
    }
}

// CSS for search result styling
const searchStyles = `
    .search-result-title {
        font-weight: 500;
        margin-bottom: 4px;
    }
    
    .search-result-content {
        font-size: 0.875rem;
        color: var(--color-text-secondary);
        margin-bottom: 4px;
        line-height: 1.4;
    }
    
    .search-result-type {
        font-size: 0.75rem;
        color: var(--color-text-muted);
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .search-result-item {
        padding: var(--space-3) var(--space-4);
        display: block;
        border-bottom: 1px solid var(--color-border-light);
        transition: background-color 0.15s ease;
    }
    
    .search-result-item:hover,
    .search-result-item.search-highlighted {
        background-color: var(--color-bg-secondary);
    }
    
    .search-result-item:last-child {
        border-bottom: none;
    }
    
    .search-result-item mark {
        background-color: var(--color-primary);
        color: white;
        padding: 1px 3px;
        border-radius: 2px;
        font-weight: 500;
    }
    
    .search-no-results {
        padding: var(--space-4);
        text-align: center;
        color: var(--color-text-secondary);
        font-size: var(--font-size-sm);
        font-style: italic;
    }
`;

// Inject search styles
const styleSheet = document.createElement('style');
styleSheet.textContent = searchStyles;
document.head.appendChild(styleSheet);

// Initialize search manager when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        window.searchManager = new SearchManager();
    });
} else {
    window.searchManager = new SearchManager();
}

// Add keyboard shortcut (Ctrl+K or Cmd+K) to focus search
document.addEventListener('keydown', (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        if (window.searchManager) {
            window.searchManager.focus();
        }
    }
});