/* ============ Data ============ */
const SKILLS = {
  backend: [
    { name: "C# / .NET", level: 85 },
    { name: "ASP.NET Core", level: 82 },
    { name: "REST API Design", level: 80 },
    { name: "Java", level: 65 },
    { name: "Python", level: 60 },
  ],
  frontend: [
    { name: "Angular", level: 78 },
    { name: "TypeScript", level: 75 },
    { name: "JavaScript", level: 78 },
    { name: "jQuery", level: 70 },
    { name: "HTML / CSS", level: 82 },
  ],
  cloud: [
    { name: "Microsoft Azure", level: 65 },
    { name: "MS SQL / PostgreSQL", level: 72 },
    { name: "Redis", level: 62 },
    { name: "Docker", level: 60 },
    { name: "Git", level: 85 },
  ],
};

const PROJECTS = [
  {
    icon: "🚢",
    title: "RS Sjøliv",
    cat: "enterprise web",
    role: "Lead Developer",
    country: "Norway",
    link: "https://sjoliv.rs.no/",
    image: "assets/img/rs-sjoliv.png",
    desc: "Course-booking platform for Redningsselskapet. Led end-to-end — upgraded to the latest .NET and integrated Vipps payments for Norwegian checkout.",
    tags: [".NET 10", "ASP.NET", "Angular", "Azure", "Redis", "Vipps"],
  },
  {
    icon: "⚓",
    title: "Trygg Båt",
    cat: "enterprise",
    role: "Backend Engineer",
    country: "Norway",
    desc: "Backend engineering for a Norwegian boat-safety platform — APIs and features on Azure, aligned with the modernized .NET stack.",
    tags: [".NET", "ASP.NET", "Azure", "REST API"],
  },
  {
    icon: "🧩",
    title: "OF — Oslofjorden",
    cat: "enterprise web",
    role: "Software Developer",
    country: "Norway",
    link: "https://www.oslofjorden.org/",
    image: "assets/img/of-platform.png",
    desc: "Digital platform for Oslofjordens Friluftsråd. Migrated to the latest .NET and integrated Vipps for memberships and bookings.",
    tags: [".NET 10", "ASP.NET", "Angular", "PostgreSQL", "Docker", "Vipps"],
  },
  {
    icon: "🏥",
    title: "MedicAid",
    cat: "web",
    role: "Full-stack",
    desc: "ASP.NET-based doctor, patient & hospital management system — appointments, medical records, billing and inventory in one streamlined platform.",
    tags: ["C#", "ASP.NET", "MS SQL", "JavaScript"],
  },
  {
    icon: "🩺",
    title: "O'Doctor",
    cat: "web",
    role: "Backend & Database",
    desc: "Comprehensive hospital management system with patient, doctor and blood-donation portals, prescriptions and full admin oversight.",
    tags: ["Java", "MySQL", "Bootstrap", "HTML"],
  },
  {
    icon: "📱",
    title: "Daily Task Manager",
    cat: "app",
    role: "Backend & Database",
    desc: "Android task manager app — add, edit, delete and complete tasks with routine notification alarms, backed by Firebase.",
    tags: ["Java", "Firebase", "Android"],
  },
  {
    icon: "🎯",
    title: "Bubble Trouble",
    cat: "app",
    role: "Developer",
    desc: "An arcade game built with the iGraphics library, focused on precise aiming and timing mechanics.",
    tags: ["C++", "iGraphics"],
  },
];

/* ============ Render skills ============ */
function renderBars(id, list) {
  const el = document.getElementById(id);
  if (!el) return;
  el.innerHTML = list
    .map(
      (s) => `
      <div class="bar">
        <div class="bar__top"><span>${s.name}</span><span>${s.level}%</span></div>
        <div class="bar__track"><div class="bar__fill" data-level="${s.level}"></div></div>
      </div>`
    )
    .join("");
}
renderBars("bars-backend", SKILLS.backend);
renderBars("bars-frontend", SKILLS.frontend);
renderBars("bars-cloud", SKILLS.cloud);

/* ============ Render projects ============ */
const FLAGS = {
  Norway:
    '<svg class="flag" viewBox="0 0 22 16" width="17" height="12" aria-hidden="true">' +
    '<rect width="22" height="16" fill="#ba0c2f"/>' +
    '<rect x="6" width="4" height="16" fill="#fff"/><rect y="6" width="22" height="4" fill="#fff"/>' +
    '<rect x="7" width="2" height="16" fill="#00205b"/><rect y="7" width="22" height="2" fill="#00205b"/>' +
    "</svg>",
};

function renderProjects() {
  const grid = document.getElementById("projectsGrid");
  if (!grid) return;
  grid.innerHTML = PROJECTS.map((p) => {
    const thumb = p.image
      ? `<a class="card__thumb" href="${p.link}" target="_blank" rel="noopener" aria-label="Visit ${p.title}">
           <img src="${p.image}" alt="${p.title} — live site screenshot" loading="lazy" />
           <span class="card__live"><span class="card__live-dot"></span>Live</span>
         </a>`
      : `<div class="card__thumb card__thumb--empty" aria-hidden="true"><span class="card__icon">${p.icon}</span></div>`;
    const icon = "";
    const country = p.country
      ? `<span class="card__country">${FLAGS[p.country] || ""}${p.country}</span>`
      : "";
    const visit = p.link
      ? `<a class="card__visit" href="${p.link}" target="_blank" rel="noopener">Visit ↗</a>`
      : "";
    const tags = p.tags.slice(0, 4).map((t) => `<span>${t}</span>`).join("");
    return `
    <article class="card reveal" data-cat="${p.cat}">
      ${thumb}
      <div class="card__body">
        ${icon}
        <div class="card__head"><h3 class="card__title">${p.title}</h3>${country}</div>
        <p class="card__desc">${p.desc}</p>
        <div class="tags">${tags}</div>
        <div class="card__foot"><span class="card__role">${p.role}</span>${visit}</div>
      </div>
    </article>`;
  }).join("");
}
renderProjects();

/* ============ Project filters ============ */
document.getElementById("filters")?.addEventListener("click", (e) => {
  const btn = e.target.closest(".filter");
  if (!btn) return;
  document.querySelectorAll(".filter").forEach((f) => f.classList.remove("is-active"));
  btn.classList.add("is-active");
  const filter = btn.dataset.filter;
  document.querySelectorAll(".card").forEach((card) => {
    const show = filter === "all" || card.dataset.cat.includes(filter);
    card.classList.toggle("is-hidden", !show);
    card.classList.add("in"); // ensure visible after filtering
  });
  const grid = document.getElementById("projectsGrid");
  if (grid) grid.scrollTo({ left: 0, behavior: "smooth" });
  setTimeout(updateNav, 350);
});

/* ============ Projects horizontal scroll ============ */
let updateNav = () => {};
(function projectsScroll() {
  const grid = document.getElementById("projectsGrid");
  const prev = document.getElementById("prevBtn");
  const next = document.getElementById("nextBtn");
  if (!grid) return;

  function step() {
    const card = grid.querySelector(".card:not(.is-hidden)");
    return (card ? card.offsetWidth : 260) + 16; // card width + gap
  }

  updateNav = function () {
    const max = grid.scrollWidth - grid.clientWidth - 2;
    const atStart = grid.scrollLeft <= 2;
    const atEnd = grid.scrollLeft >= max;
    const noScroll = grid.scrollWidth <= grid.clientWidth + 4;
    if (prev) prev.disabled = atStart || noScroll;
    if (next) next.disabled = atEnd || noScroll;
  };

  prev?.addEventListener("click", () => grid.scrollBy({ left: -step(), behavior: "smooth" }));
  next?.addEventListener("click", () => grid.scrollBy({ left: step(), behavior: "smooth" }));
  grid.addEventListener("scroll", updateNav, { passive: true });
  window.addEventListener("resize", updateNav);
  requestAnimationFrame(updateNav);
})();

/* ============ Typed role effect ============ */
(function typedEffect() {
  const el = document.getElementById("typed");
  if (!el) return;
  const roles = [
    "Software Engineer II",
    ".NET Developer",
    "Angular Developer",
    "Competitive Programmer",
    "Problem Solver",
  ];
  let r = 0, c = 0, deleting = false;
  function tick() {
    const word = roles[r];
    el.textContent = word.slice(0, c);
    if (!deleting && c < word.length) {
      c++;
      setTimeout(tick, 80);
    } else if (deleting && c > 0) {
      c--;
      setTimeout(tick, 40);
    } else {
      if (!deleting) {
        deleting = true;
        setTimeout(tick, 1600);
      } else {
        deleting = false;
        r = (r + 1) % roles.length;
        setTimeout(tick, 300);
      }
    }
  }
  tick();
})();

/* ============ Theme toggle ============ */
(function theme() {
  const root = document.documentElement;
  const btn = document.getElementById("themeToggle");
  const saved = localStorage.getItem("theme");
  if (saved) root.setAttribute("data-theme", saved);
  btn?.addEventListener("click", () => {
    const next = root.getAttribute("data-theme") === "light" ? "dark" : "light";
    root.setAttribute("data-theme", next);
    localStorage.setItem("theme", next);
  });
})();

/* ============ Mobile nav ============ */
(function mobileNav() {
  const toggle = document.getElementById("navToggle");
  const links = document.getElementById("navLinks");
  toggle?.addEventListener("click", () => {
    toggle.classList.toggle("open");
    links.classList.toggle("open");
  });
  links?.querySelectorAll("a").forEach((a) =>
    a.addEventListener("click", () => {
      toggle.classList.remove("open");
      links.classList.remove("open");
    })
  );
})();

/* ============ Navbar scroll + progress + active link ============ */
(function scrollFx() {
  const nav = document.getElementById("nav");
  const progress = document.getElementById("scrollProgress");
  const links = [...document.querySelectorAll('.nav__links a')];
  const sections = links
    .map((l) => document.querySelector(l.getAttribute("href")))
    .filter(Boolean);

  function onScroll() {
    const y = window.scrollY;
    nav.classList.toggle("scrolled", y > 30);
    const h = document.documentElement.scrollHeight - window.innerHeight;
    progress.style.width = (y / h) * 100 + "%";

    let current = sections[0]?.id;
    for (const s of sections) {
      if (y >= s.offsetTop - 120) current = s.id;
    }
    links.forEach((l) =>
      l.classList.toggle("active", l.getAttribute("href") === "#" + current)
    );
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();
})();

/* ============ Reveal on scroll + counters + bars ============ */
(function reveal() {
  const io = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("in");

        // animate skill bars inside
        entry.target.querySelectorAll?.(".bar__fill").forEach((f) => {
          f.style.width = f.dataset.level + "%";
        });

        // animate counters
        if (entry.target.classList.contains("stat")) {
          const num = entry.target.querySelector(".stat__num");
          animateCount(num);
        }
        io.unobserve(entry.target);
      });
    },
    { threshold: 0.15 }
  );

  document.querySelectorAll(".reveal").forEach((el) => io.observe(el));

  // observe skill groups explicitly so bars fill
  document.querySelectorAll(".skill-group").forEach((el) => io.observe(el));
})();

function animateCount(el) {
  if (!el) return;
  const target = +el.dataset.target;
  const suffix = el.dataset.suffix || "";
  const dur = 1600;
  const start = performance.now();
  function step(now) {
    const p = Math.min((now - start) / dur, 1);
    const eased = 1 - Math.pow(1 - p, 3);
    el.textContent = Math.floor(eased * target).toLocaleString() + (p === 1 ? suffix : "");
    if (p < 1) requestAnimationFrame(step);
  }
  requestAnimationFrame(step);
}

/* ============ Year ============ */
document.getElementById("year").textContent = new Date().getFullYear();
