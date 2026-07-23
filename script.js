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
    title: "RS Sjoliv",
    cat: "enterprise web",
    role: "Lead Developer",
    desc: "Led end-to-end development of an enterprise platform — system design, backend, frontend and database — delivering a highly scalable, reliable solution with measurable performance gains.",
    tags: ["ASP.NET", "Angular", "Azure", "Redis"],
  },
  {
    icon: "⚓",
    title: "Trygg Båt",
    cat: "enterprise",
    role: "Backend Engineer",
    desc: "Backend engineering for a boat-safety platform, covering system design, API development and feature implementation on Azure.",
    tags: ["ASP.NET", "Azure", "REST API"],
  },
  {
    icon: "🧩",
    title: "OF Platform",
    cat: "enterprise web",
    role: "Software Developer",
    desc: "Delivered end-to-end features — architected scalable system design, optimized complex database structures and built robust backend services with intuitive frontend interfaces.",
    tags: ["ASP.NET", "Angular", "PostgreSQL", "Docker", "Redis"],
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
function renderProjects() {
  const grid = document.getElementById("projectsGrid");
  if (!grid) return;
  grid.innerHTML = PROJECTS.map(
    (p) => `
    <article class="card reveal" data-cat="${p.cat}">
      <div class="card__icon">${p.icon}</div>
      <h3 class="card__title">${p.title}</h3>
      <p class="card__desc">${p.desc}</p>
      <div class="tags">${p.tags.map((t) => `<span>${t}</span>`).join("")}</div>
      <div class="card__foot"><span class="card__role">${p.role}</span></div>
    </article>`
  ).join("");
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
  });
});

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
