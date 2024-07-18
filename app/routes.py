from flask import render_template
from app import app

# Sample data for courses
courses = [
    {
        'title': 'CS 8, 16, 24, 32',
        'description': 'Variables, Functions, Loops, Arrays/Vectors, Branches, Pointers, Struct, Linked Lists, Recursion, Constructors, String Stream, Heap/Stack, Encapsulation, Polymorphism, Inheritance',
    },
    {
        'title': 'ECE 15A',
        'description': 'Boolean algebra, logic of propositions, minterm and maxterm expansions, Karnaugh maps, Quine-McCluskey methods, multi-level circuits, combinational circuit design and simulation, multiplexers, decoders, programmable logic devices',
    },
    {
        'title': 'ECE 152A',
        'description': 'Design of synchronous digital systems: timing diagrams, propagation delay, latches and flip-flops, shift registers and counters, Mealy/Moore finite state machines, Verilog, 2-phase clocking, timing analysis, CMOS implementation, RAM-based designs, ASM charts, state minimization',
    },
    {
        'title': 'ECE 10A, 10B, 10C',
        'description': 'Resistive networks, network analysis, MOSFET, small-signal analysis, BJT, op-amps, first-order and second-order linear time invariant circuits, sinusoidal steady state, impedance representation, feedback and resonance',
    },
    {
        'title': 'CS 40',
        'description': 'Propositional predicate logic, set theory, functions and relations, counting, mathematical induction, recursion',
    },
    {
        'title': 'ECE 154A, 154B',
        'description': 'Instruction-set architecture (ISA) and computer performance; Machine instructions, assembly; Memory map; Procedure calls; Number formats; Simple ALUs; Pipelined data paths and control schemes; Cache and virtual memory; Disk arrays; Instruction-level parallelism',
    },
    {
        'title': 'ECE 157A, 157B',
        'description': 'Introduces an artificial intelligence system view to apply machine learning to improve hardware design and test automation processes',
    },
    {
        'title': 'CS 130A',
        'description': 'DFS/BFS, Dijkstra, Bellman-Ford, Topological Sort, MST (Prim and Kruskal), Hash Tables, AVL rotations, insertions, removals',
    },
    {
        'title': 'ECE 153A',
        'description': 'Issues in interfacing computing systems and software to practical I/O interfaces. Rapid response, realtime events and management of tasks, threads, and scheduling',
    },
    {
        'title': 'ECE 153B',
        'description': 'Hardware description languages; field-programmable logic and ASIC design techniques. Mixed signal techniques: ADC/DAC; video and audio signal acquisition, processing and generation, communication and network interfaces',
    },
    {
        'title': 'CS 170',
        'description': 'Process; interprocess communication and synchronization; input-output, file systems, memory management',
    },
    {
        'title': 'CS 156',
        'description': 'Generic programming, exception handling, application development, third-party library use, version control, software testing, issue tracking, code review, working with legacy code',
    },
    {
        'title': 'CS 171',
        'description': 'Distributed systems architecture, distributed programming, network of computers, message passing, remote procedure calls, group communication, naming and membership problems, asynchrony, logical time, consistency, fault-tolerance, recovery.',
    },
    {
        'title': 'CS 177',
        'description': 'Introduction to the basics of computer security and privacy. Analysis of technical difficulties of producing secure computer information systems that provide guaranteed controlled sharing. Examination and critique of current systems, methods, certification.',
    }
]

@app.route('/')
def index():
    return render_template('index.html', courses=courses)
